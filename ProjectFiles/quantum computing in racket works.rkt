#lang plait


(define-type Exp
  (qubitE [zero : Number]
          [one : Number]))


(module+ test
  (print-only-errors #t))

;; parse ----------------------------------------
(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `"|0>" s) (qubitE 1 0)] 
    [(s-exp-match?  `"|1>" s) (qubitE 0 1)]
    [else (error 'parse "invalid input")]))

(module+ test
  (test (parse `"|0>")
        (qubitE 1 0))
  (test (parse `"|1>")
        (qubitE 0 1))
  (test/exn (parse `{{+ 1 2}})
            "invalid input")
  )

