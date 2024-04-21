#lang racket

; Parses a single line to generate Python code.
(define (parse-line line)
  (let* ((parts (string-split line " "))  ; Use " " as the delimiter
         (prefix (string-trim (first parts) "|")))
    (define qubit-content (regexp-replace* #rx"[^0-9-]" prefix "")) ; Extract only digits and "-"
    (string-append
     (if (string=? qubit-content "")
         ""
         (string-append "q = qubit([" qubit-content "])\nprint(q)\n")))))

; Reads a file and parses each line to generate Python code.
(define (read-file filename)
  (with-input-from-file filename
    (lambda ()
      (let loop ((lines '()))
        (let ((line (read-line)))
          (if (eof-object? line)
              (string-join (reverse lines) "")
              (loop (cons (parse-line line) lines))))))))

; Appends the generated Python code to an existing Python file.
(define (append-to-py-file filename python_code)
  (call-with-output-file filename
    #:exists 'append
    (lambda (output-port)
      (display python_code output-port))))

; Function that runs the script.
(define (main input-file output-file)
  (let ((python-code (read-file input-file)))
    (append-to-py-file output-file python-code)))

; Parse command-line arguments.
(define input-file (vector-ref (current-command-line-arguments) 0))
(define output-file (vector-ref (current-command-line-arguments) 1))

; Execute the main function with input and output file paths.
(main input-file output-file)
