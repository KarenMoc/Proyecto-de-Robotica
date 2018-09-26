
#include <ros.h>
#include <geometry_msgs/Vector3.h>
#include <std_msgs/String.h>
#include "DualMC33926MotorShield.h"

DualMC33926MotorShield md;
ros::NodeHandle  nh;



// Set speed variables
geometry_msgs::Vector3 motor_speed_set;
geometry_msgs::Vector3 str_msg;

ros::Publisher flag("chatter", &str_msg);


// Callbacks for motor speed

void set_speed( const geometry_msgs::Vector3& motor_speed_set){
  // Left motor
  md.setM2Speed(map(motor_speed_set.x, -1, 1, -400,400));
  str_msg= motor_speed_set;
  flag.publish( &str_msg );
  // Right motor
  md.setM1Speed(map(motor_speed_set.y, -1, 1, -400,400));
}


// Velocity subscribers
ros::Subscriber<geometry_msgs::Vector3> motor_controller("filter_joy", &set_speed );





void setup()
{
  md.init();
  // Right motor
  md.setM1Speed(0);
  // Left motor
  md.setM2Speed(0);
  
  nh.initNode();
  nh.advertise(flag);
  nh.subscribe(motor_controller);
}

void loop()
{

  
  /*
  str_msg.data = hello;
  chatter.publish( &str_msg );

  */

  

  nh.spinOnce();
  delay(100);
}
