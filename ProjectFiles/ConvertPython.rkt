#lang racket

(define (read-file filename)
  (with-input-from-file filename
    (lambda ()
      (let loop ((line (read-line)))
        (cond
          [(eof-object? line) '()]
          [else (cons line (loop (read-line)))])))))

(define (write-to-py-file filename python_code)
  (with-output-to-file filename
    (lambda ()
      (display python_code))))

(define lines (read-file ""))

(write-to-py-file "" (string-join lines "\n"))
