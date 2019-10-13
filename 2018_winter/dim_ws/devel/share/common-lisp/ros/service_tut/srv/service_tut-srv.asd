
(cl:in-package :asdf)

(defsystem "service_tut-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "myservice" :depends-on ("_package_myservice"))
    (:file "_package_myservice" :depends-on ("_package"))
  ))