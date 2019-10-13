;; Auto-generated. Do not edit!


(when (boundp 'dim::myservice)
  (if (not (find-package "DIM"))
    (make-package "DIM"))
  (shadow 'myservice (find-package "DIM")))
(unless (find-package "DIM::MYSERVICE")
  (make-package "DIM::MYSERVICE"))
(unless (find-package "DIM::MYSERVICEREQUEST")
  (make-package "DIM::MYSERVICEREQUEST"))
(unless (find-package "DIM::MYSERVICERESPONSE")
  (make-package "DIM::MYSERVICERESPONSE"))

(in-package "ROS")





(defclass dim::myserviceRequest
  :super ros::object
  :slots (_req ))

(defmethod dim::myserviceRequest
  (:init
   (&key
    ((:req __req) "")
    )
   (send-super :init)
   (setq _req (string __req))
   self)
  (:req
   (&optional __req)
   (if __req (setq _req __req)) _req)
  (:serialization-length
   ()
   (+
    ;; string _req
    4 (length _req)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _req
       (write-long (length _req) s) (princ _req s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _req
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _req (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass dim::myserviceResponse
  :super ros::object
  :slots (_res ))

(defmethod dim::myserviceResponse
  (:init
   (&key
    ((:res __res) "")
    )
   (send-super :init)
   (setq _res (string __res))
   self)
  (:res
   (&optional __res)
   (if __res (setq _res __res)) _res)
  (:serialization-length
   ()
   (+
    ;; string _res
    4 (length _res)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _res
       (write-long (length _res) s) (princ _res s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _res
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _res (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass dim::myservice
  :super ros::object
  :slots ())

(setf (get dim::myservice :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get dim::myservice :datatype-) "dim/myservice")
(setf (get dim::myservice :request) dim::myserviceRequest)
(setf (get dim::myservice :response) dim::myserviceResponse)

(defmethod dim::myserviceRequest
  (:response () (instance dim::myserviceResponse :init)))

(setf (get dim::myserviceRequest :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get dim::myserviceRequest :datatype-) "dim/myserviceRequest")
(setf (get dim::myserviceRequest :definition-)
      "string req
---
string res

")

(setf (get dim::myserviceResponse :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get dim::myserviceResponse :datatype-) "dim/myserviceResponse")
(setf (get dim::myserviceResponse :definition-)
      "string req
---
string res

")



(provide :dim/myservice "fd72814fc41c6bccdf8759d8dea09f77")


