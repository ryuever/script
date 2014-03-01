/* Sample implementation of wc utility. */
/* Extend wc with the function of counting the numbers of Chinese and Japanese characters  
 *  
 * Copyright 2014 ryuyutyo<liuyouchao111@gmail.com>
 *
 * Because utf-8 code of Chinese or Japanese characters are 3 bytes length and the firt
 * byte is greater than 0xe3.
 *
 * Based on the condition once read a char greater than 0xe3, continue to read 
 * the following two bytes without any processing except for incrementing ccount. These 
 * 3 bytes will be regarded as a word.
*/
   
#include <stdlib.h>
#include <stdio.h>
#include <stdarg.h>
     
typedef unsigned long count_t;  /* Counter type */
     
/* Current file counters: chars, words, lines */
count_t ccount;
count_t wcount;
count_t lcount;
     
/* Totals counters: chars, words, lines */
count_t total_ccount = 0;
count_t total_wcount = 0;
count_t total_lcount = 0;
     
/* Print error message and exit with error status. If PERR is not 0,
   display current errno status. */
static void error_print (int perr, char *fmt, va_list ap){
  vfprintf (stderr, fmt, ap);
  if (perr)
    perror (" ");
  else
    fprintf (stderr, "\n");
  exit (1);  
}
     
/* Print error message and exit with error status. */
static void errf (char *fmt, ...){
  va_list ap;
       
  va_start (ap, fmt);
  error_print (0, fmt, ap);
  va_end (ap);
}
     
/* Print error message followed by errno status and exit
   with error code. */
static void perrf (char *fmt, ...){
  va_list ap;
       
  va_start (ap, fmt);
  error_print (1, fmt, ap);
  va_end (ap);
}
     
/* Output counters for given file */
void report (char *file, count_t ccount, count_t wcount, count_t lcount){
  printf ("%6lu %6lu %6lu %s\n", lcount, wcount, ccount, file);
}
     
/* Return true if C is a valid word constituent */
static int isword (unsigned char c){
  return isalpha (c);
}
     
/* Increase character and, if necessary, line counters */
#define COUNT(c)                                \
  ccount++;                                     \
  if ((c) == '\n')                              \
    lcount++;
     
/* Get next word from the input stream. Return 0 on end
   of file or error condition. Return 1 otherwise. */
int getword (FILE *fp){
  int c;
  int word = 0;
       
  if (feof (fp))
    return 0;
           
  while ((c = getc (fp)) != EOF){
    /* If the first byte is an alphabet, then increment wcount by 1 
       and skip from while statement goto the following for loop to 
       to read the remainding part of this word
    */    
    if (isword (c)){        
      wcount++;
      break;
    }
    
    for(; c>= 0xe3;){
      wcount++;
      getc(fp);
      getc(fp);
      ccount = ccount + 3;
      return c != EOF;       // back to stream to read next word
    }

    // if it is non-alphabet, increment ccount. 
    COUNT (c);               
  }
     
  for (; c != EOF; c = getc (fp)){
    COUNT (c);     // increment ccount first, so the following for loop add 2 
    
    // "a痒" is regarded as two words. This for loop is used for processing 
    // the situation. alphabet is immediately followed by a Chinese character.
    for(; c> 0xe3;){
      wcount++;
      getc(fp);
      getc(fp);
      ccount = ccount + 2;
      return c != EOF;
    }

    if (!isword (c))
      break;
  }

  // back to stream to read a next word
  return c != EOF;      
}
           
/* Process file FILE. */
void counter (char *file){
  FILE *fp = fopen (file, "r");
       
  if (!fp)
    perrf ("cannot open file `%s'", file);
     
  ccount = wcount = lcount = 0;
  while (getword (fp))
    ;
  fclose (fp);
     
  report (file, ccount, wcount, lcount);
  total_ccount += ccount;
  total_wcount += wcount;
  total_lcount += lcount;
}
       
int main (int argc, char **argv){
  int i;
       
  if (argc < 2)
    errf ("usage: wc FILE [FILE...]");
       
  for (i = 1; i < argc; i++)
    counter (argv[i]);
       
  if (argc > 2)
    report ("total", total_ccount, total_wcount, total_lcount);
  return 0;
}
