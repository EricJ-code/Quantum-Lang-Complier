#lang racket

(define (parse-line line)
  (define cleaned-line (regexp-replace #rx"\r" line ""))
  (match (string-split cleaned-line " ")
    [(list "|0>" var-name)
     (format "~a = qubit([0]) \n" var-name)]
    [(list "|1>" var-name)
     (format "~a = qubit([1]) \n" var-name)]
    [(list var-name "=" "gate()")
     (format "~a = gate() \n" var-name)]
    [(list (regexp #rx"([a-zA-Z0-9_]+).(h|x|y|z)") var-name)
     (define gate (second (regexp-match #rx"([a-zA-Z0-9_]+).(h|x|y|z)" (first (string-split cleaned-line " ")))))
     (define operation (third (regexp-match #rx"([a-zA-Z0-9_]+).(h|x|y|z)" (first (string-split cleaned-line " ")))))
     (format "~a.default_gates('~a', ~a) \n" gate operation var-name)]
    [(list "observe" var-name)
     (format "print(~a) \n" var-name)]
    [else
     ""])) ; Return an empty string if no pattern matches

(define (read-file filename)
  (with-input-from-file filename
    (lambda ()
      (let loop ((lines '()))
        (let ((line (read-line)))
          (if (eof-object? line)
              (string-join (reverse lines) "")
              (let ((parsed-line (parse-line line)))
                (loop (cons parsed-line lines)))))))))

(define (append-to-py-file filename python_code)
  (with-output-to-file filename
    #:exists 'append
    #:mode 'text
    (lambda ()
      (for-each (lambda (line)
                  (display line)
                  (newline))
                (string-split python_code "\n")))))

(define (main input-file output-file)
  (let ((python-code (read-file input-file)))
    (append-to-py-file output-file python-code)))

(main (vector-ref (current-command-line-arguments) 0)
      (vector-ref (current-command-line-arguments) 1))
