#!/usr/bin/env python
import rospy
from std_msgs.msg import String


class Player:
    def __init__(self, player_name):
        self.player_name = player_name


        red_team = rospy.get_param('/red_team')
        blue_team = rospy.get_param('/blue_team')
        green_team = rospy.get_param('/green_team')

        print('red_team = ' + str(red_team))
        print('blue_team = ' + str(blue_team))
        print('green_team = ' + str(green_team))

        if self.player_name in red_team:
            self.my_team, self.prey_team, self.hunter_team = 'red', 'green', 'blue'
            self.my_players, self.preys, self.hunters = red_team, green_team, blue_team
        elif self.player_name in green_team:
            self.my_team, self.prey_team, self.hunter_team = 'green', 'blue', 'red'
            self.my_players, self.preys, self.hunters = green_team, blue_team, red_team
        elif self.player_name in blue_team:
            self.my_team, self.prey_team, self.hunter_team = 'blue', 'red', 'green'
            self.my_players, self.preys, self.hunters = blue_team, red_team, green_team
        else:
            rospy.logerr('my name is not in any team, let me play')
            exit(0)

        rospy.logwarn('I am ' + self.player_name + ' and I am on team ' + self.my_team + '. ' + self.prey_team + 'players are all going to die')
        rospy.logwarn('I am running from ' + str(self.hunters))

def callback(msg):
    print("received a message containing string" + msg.data)

def main():
    print("hello player node")

    rospy.init_node('dfigueiredo', anonymous=False)

    player = Player('dfigueiredo')
    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ =="__main__":
    main()