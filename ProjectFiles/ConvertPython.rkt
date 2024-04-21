#lang racket

; Reads a file and returns it as a list of lines that is an s-expression.
(define (read-file filename)
  (with-input-from-file filename
    (lambda ()
      (let loop ((lines '()))
        (let ((line (read-line)))
          (if (eof-object? line)
              (reverse lines)
              (loop (cons line lines))))))))

; Writes a string to python file.
(define (write-to-py-file filename python_code)
  (with-output-to-file filename
    (lambda ()
      (display python_code))))

; Function that runs the script.
(define (main input-file output-file)
  (let ((lines (read-file input-file)))
    (write-to-py-file output-file (string-join lines "\n"))))

; Parse to command line.
(define input-file (vector-ref (current-command-line-arguments) 0))
(define output-file (vector-ref (current-command-line-arguments) 1))

(main input-file output-file)
