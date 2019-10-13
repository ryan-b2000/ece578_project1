;; Auto-generated. Do not edit!


(when (boundp 'service_tut::myservice)
  (if (not (find-package "SERVICE_TUT"))
    (make-package "SERVICE_TUT"))
  (shadow 'myservice (find-package "SERVICE_TUT")))
(unless (find-package "SERVICE_TUT::MYSERVICE")
  (make-package "SERVICE_TUT::MYSERVICE"))
(unless (find-package "SERVICE_TUT::MYSERVICEREQUEST")
  (make-package "SERVICE_TUT::MYSERVICEREQUEST"))
(unless (find-package "SERVICE_TUT::MYSERVICERESPONSE")
  (make-package "SERVICE_TUT::MYSERVICERESPONSE"))

(in-package "ROS")





(defclass service_tut::myserviceRequest
  :super ros::object
  :slots (_req ))

(defmethod service_tut::myserviceRequest
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

(defclass service_tut::myserviceResponse
  :super ros::object
  :slots (_res ))

(defmethod service_tut::myserviceResponse
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

(defclass service_tut::myservice
  :super ros::object
  :slots ())

(setf (get service_tut::myservice :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get service_tut::myservice :datatype-) "service_tut/myservice")
(setf (get service_tut::myservice :request) service_tut::myserviceRequest)
(setf (get service_tut::myservice :response) service_tut::myserviceResponse)

(defmethod service_tut::myserviceRequest
  (:response () (instance service_tut::myserviceResponse :init)))

(setf (get service_tut::myserviceRequest :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get service_tut::myserviceRequest :datatype-) "service_tut/myserviceRequest")
(setf (get service_tut::myserviceRequest :definition-)
      "string req
---
string res


")

(setf (get service_tut::myserviceResponse :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get service_tut::myserviceResponse :datatype-) "service_tut/myserviceResponse")
(setf (get service_tut::myserviceResponse :definition-)
      "string req
---
string res


")



(provide :service_tut/myservice "fd72814fc41c6bccdf8759d8dea09f77")


