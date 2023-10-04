import rclpy
from rclpy.node import Node
from robot_action_interfaces.srv import GetRobotPose  # Import the updated service message
from geometry_msgs.msg import PoseStamped

class RobotPoseService(Node):

    def __init__(self):
        super().__init__('robot_pose_service')
        self.robot_pose = PoseStamped()
        self.pose_subscription = self.create_subscription(
            PoseStamped,
            '/map_pose',  # Topic on which pose is being relayed
            self.pose_callback,
            10  # Adjust the queue size as needed
        )
        self.pose_subscription 

        # Create the service server
        self.robot_pose_service = self.create_service(
            GetRobotPose,
            'get_robot_pose',
            self.get_robot_pose_callback
        )

    def pose_callback(self, msg):
        # Callback function for the /map_pose topic
        self.robot_pose = msg

    def get_robot_pose_callback(self, request, response):
        response.robot_pose = self.robot_pose
        return response

def main(args=None):
    rclpy.init(args=args)
    robot_pose_service = RobotPoseService()
    rclpy.spin(robot_pose_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
