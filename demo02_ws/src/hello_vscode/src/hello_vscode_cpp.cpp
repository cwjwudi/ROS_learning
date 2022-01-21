#include "ros/ros.h"

int main(int argc, char *argv[])
{
    //解决乱码
    setlocale(LC_ALL,"");

    ros::init(argc,argv,"hello_text");

    ROS_INFO("hahahahaha 哈哈哈哈哈");
    /* code */
    return 0;
}
