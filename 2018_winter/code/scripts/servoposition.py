import rospy
import time
from dynamixel_msgs.msg import JointState
from std_msgs.msg import Float64
from std_msgs.msg import String
from std_msgs.msg import Int32
import os

global in_action
in_action = 0


#NEED HIMANSHU TO tell me nodes setup for ROS servocs
#pub1  = rospy.Publisher('/head_controller/command', Float64,queue_size=20)
#pub2  = rospy.Publisher('/neck_controller/command', Float64,queue_size=20)
pub3  = rospy.Publisher('/right_shoulder_controller/command', Float64,queue_size=20)
pub4  = rospy.Publisher('/left_shoulder_controller/command', Float64,queue_size=20)
pub5  = rospy.Publisher('/left_upper_controller/command', Float64,queue_size=20)
pub6  = rospy.Publisher('/left_lower_controller/command', Float64,queue_size=20)
pub7  = rospy.Publisher('/left_elbow_controller/command', Float64,queue_size=20)
pub8  = rospy.Publisher('/right_upper_controller/command', Float64,queue_size=20)
pub9  = rospy.Publisher('/right_lower_controller/command', Float64,queue_size=20)
pub10 = rospy.Publisher('/right_elbow_controller/command', Float64,queue_size=20)



def lineCallback(data):
    print("motion")
    line = data.data
    global in_action
    if in_action == 0:
        in_action = 1	
        if(line == 1):
            #OPEN MOUTH  a bit
            "Open arms wide CALM FACE
        
        if(line = 8):
        #smile goofy 
        if(line = 10):
            #put arms out to both sides with calm face
         
         pub1.publish(float(joint_positions[0]))
                    pub2.publish(float(joint_positions[1]))
                    pub3.publish(float(joint_positions[2]))
                    pub4.publish(float(joint_positions[3]))
                    pub5.publish(float(joint_positions[4]))
                    pub6.publish(float(joint_positions[5]))
                    pub7.publish(float(joint_positions[6]))
                    pub8.publish(float(joint_positions[7]))
                    pub9.publish(float(joint_positions[8]))
                    pub10.publish(float(joint_positions[9]))
                    # delay between motions
                    rospy.sleep(float(delay))
                in_action = 0
                print("motion is done")
        except:
            in_action = 0
            print("motion file doesn't exist")
    else:
        print("The robot can't play this motion because it is playing another motion. Wait until the motion is done.")


rospy.Subscriber("/lines",Int32,lineCallback)
if __name__ == '__main__':
    try:
        rospy.init_node('head_controller', anonymous=True)
	#print("eNTERED")
    #    motion_play()
	rospy.spin()

    except rospy.ROSInterruptException:
        pass
