import rospy
from geometry_msgs.msg import Twist


def move_robot():
    rospy.init_node('robot_controller')  # Initialize the ROS node with the name 'robot_controller'
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # Create a publisher to the /cmd_vel topic
    rate = rospy.Rate(10)  # Set the loop frequency to 10 Hz

    while not rospy.is_shutdown():
        twist = Twist()  # Create a new Twist message
        twist.linear.x = 0.2  # Set linear velocity in x (forward speed)
        twist.angular.z = 0.1  # Set angular velocity in z (rotation)
        pub.publish(twist)  # Publish the velocity command
        rate.sleep()  # Sleep to maintain the loop rate


if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
