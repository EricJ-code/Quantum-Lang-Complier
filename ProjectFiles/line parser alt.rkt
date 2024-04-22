#lang racket

(define (parse-line line)
  (match (string-split line " ")
    [(list "|0>" var-name)
     (format "~a = qubit(0)\n" var-name)]
    [(list "|1>" var-name)
     (format "~a = qubit(1)\n" var-name)]
    ; Handle different variable names for gate operations
    [(list (regexp #rx"([a-zA-Z0-9_]+).(h|x|y|z)") var-name)
     (define gate (second (regexp-match #rx"([a-zA-Z0-9_]+).(h|x|y|z)" (first (string-split line " ")))))
     (define operation (third (regexp-match #rx"([a-zA-Z0-9_]+).(h|x|y|z)" (first (string-split line " ")))))
     (format "~a.default_gates('~a', ~a)\n" gate operation var-name)]
    [else
     ""])) ; Return an empty string if no pattern matches

;; Example usage:
(parse-line "|0> qubit1")
(parse-line "|1> qubit1")
(parse-line "fuck.h qubit1")
(parse-line "this.x qubit2")
(parse-line "shit.y qubit3")
(parse-line "g.z qubit4")
(parse-line "observe")
