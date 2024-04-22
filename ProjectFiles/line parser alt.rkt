#lang racket

(define (parse-line line)
  (match (string-split line " ")
    ;; Match qubit initializations
    [(list "|0>" var-name)
     (format "~a = qubit(0)" var-name)]
    [(list "|1>" var-name)
     (format "~a = qubit(1)" var-name)]
    ;; Match default gates calls
    [(list "g.h" var-name)
     (format "g.default_gates('h', ~a)" var-name)]
    [(list "g.x" var-name)
     (format "g.default_gates('x', ~a)" var-name)]
    [(list "g.y" var-name)
     (format "g.default_gates('y', ~a)" var-name)]
    [(list "g.z" var-name)
     (format "g.default_gates('z', ~a)" var-name)]
    ;; Handle unrecognized patterns
    [_
     (error "Unrecognized pattern")]))

;; Example usage:
(parse-line "|0> qubit1")
(parse-line "|1> qubit1")
(parse-line "g.h qubit1")
(parse-line "g.x qubit2")
(parse-line "g.y qubit3")
(parse-line "g.z qubit4")
(parse-line "observe")
