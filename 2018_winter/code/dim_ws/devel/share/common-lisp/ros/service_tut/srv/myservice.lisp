; Auto-generated. Do not edit!


(cl:in-package service_tut-srv)


;//! \htmlinclude myservice-request.msg.html

(cl:defclass <myservice-request> (roslisp-msg-protocol:ros-message)
  ((req
    :reader req
    :initarg :req
    :type cl:string
    :initform ""))
)

(cl:defclass myservice-request (<myservice-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <myservice-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'myservice-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name service_tut-srv:<myservice-request> is deprecated: use service_tut-srv:myservice-request instead.")))

(cl:ensure-generic-function 'req-val :lambda-list '(m))
(cl:defmethod req-val ((m <myservice-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader service_tut-srv:req-val is deprecated.  Use service_tut-srv:req instead.")
  (req m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <myservice-request>) ostream)
  "Serializes a message object of type '<myservice-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'req))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'req))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <myservice-request>) istream)
  "Deserializes a message object of type '<myservice-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'req) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'req) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<myservice-request>)))
  "Returns string type for a service object of type '<myservice-request>"
  "service_tut/myserviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'myservice-request)))
  "Returns string type for a service object of type 'myservice-request"
  "service_tut/myserviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<myservice-request>)))
  "Returns md5sum for a message object of type '<myservice-request>"
  "fd72814fc41c6bccdf8759d8dea09f77")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'myservice-request)))
  "Returns md5sum for a message object of type 'myservice-request"
  "fd72814fc41c6bccdf8759d8dea09f77")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<myservice-request>)))
  "Returns full string definition for message of type '<myservice-request>"
  (cl:format cl:nil "string req~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'myservice-request)))
  "Returns full string definition for message of type 'myservice-request"
  (cl:format cl:nil "string req~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <myservice-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'req))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <myservice-request>))
  "Converts a ROS message object to a list"
  (cl:list 'myservice-request
    (cl:cons ':req (req msg))
))
;//! \htmlinclude myservice-response.msg.html

(cl:defclass <myservice-response> (roslisp-msg-protocol:ros-message)
  ((res
    :reader res
    :initarg :res
    :type cl:string
    :initform ""))
)

(cl:defclass myservice-response (<myservice-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <myservice-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'myservice-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name service_tut-srv:<myservice-response> is deprecated: use service_tut-srv:myservice-response instead.")))

(cl:ensure-generic-function 'res-val :lambda-list '(m))
(cl:defmethod res-val ((m <myservice-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader service_tut-srv:res-val is deprecated.  Use service_tut-srv:res instead.")
  (res m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <myservice-response>) ostream)
  "Serializes a message object of type '<myservice-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'res))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'res))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <myservice-response>) istream)
  "Deserializes a message object of type '<myservice-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'res) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'res) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<myservice-response>)))
  "Returns string type for a service object of type '<myservice-response>"
  "service_tut/myserviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'myservice-response)))
  "Returns string type for a service object of type 'myservice-response"
  "service_tut/myserviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<myservice-response>)))
  "Returns md5sum for a message object of type '<myservice-response>"
  "fd72814fc41c6bccdf8759d8dea09f77")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'myservice-response)))
  "Returns md5sum for a message object of type 'myservice-response"
  "fd72814fc41c6bccdf8759d8dea09f77")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<myservice-response>)))
  "Returns full string definition for message of type '<myservice-response>"
  (cl:format cl:nil "string res~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'myservice-response)))
  "Returns full string definition for message of type 'myservice-response"
  (cl:format cl:nil "string res~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <myservice-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'res))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <myservice-response>))
  "Converts a ROS message object to a list"
  (cl:list 'myservice-response
    (cl:cons ':res (res msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'myservice)))
  'myservice-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'myservice)))
  'myservice-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'myservice)))
  "Returns string type for a service object of type '<myservice>"
  "service_tut/myservice")