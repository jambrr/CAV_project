// Generated by gencpp from file dbw_mkz_msgs/ParkingBrake.msg
// DO NOT EDIT!


#ifndef DBW_MKZ_MSGS_MESSAGE_PARKINGBRAKE_H
#define DBW_MKZ_MSGS_MESSAGE_PARKINGBRAKE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace dbw_mkz_msgs
{
template <class ContainerAllocator>
struct ParkingBrake_
{
  typedef ParkingBrake_<ContainerAllocator> Type;

  ParkingBrake_()
    : status(0)  {
    }
  ParkingBrake_(const ContainerAllocator& _alloc)
    : status(0)  {
  (void)_alloc;
    }



   typedef uint8_t _status_type;
  _status_type status;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(OFF)
  #undef OFF
#endif
#if defined(_WIN32) && defined(TRANS)
  #undef TRANS
#endif
#if defined(_WIN32) && defined(ON)
  #undef ON
#endif
#if defined(_WIN32) && defined(FAULT)
  #undef FAULT
#endif

  enum {
    OFF = 0u,
    TRANS = 1u,
    ON = 2u,
    FAULT = 3u,
  };


  typedef boost::shared_ptr< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> const> ConstPtr;

}; // struct ParkingBrake_

typedef ::dbw_mkz_msgs::ParkingBrake_<std::allocator<void> > ParkingBrake;

typedef boost::shared_ptr< ::dbw_mkz_msgs::ParkingBrake > ParkingBrakePtr;
typedef boost::shared_ptr< ::dbw_mkz_msgs::ParkingBrake const> ParkingBrakeConstPtr;

// constants requiring out of line definition

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator1> & lhs, const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator2> & rhs)
{
  return lhs.status == rhs.status;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator1> & lhs, const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dbw_mkz_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2280b2c9c46fd98be0f067aa92f74fc4";
  }

  static const char* value(const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2280b2c9c46fd98bULL;
  static const uint64_t static_value2 = 0xe0f067aa92f74fc4ULL;
};

template<class ContainerAllocator>
struct DataType< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dbw_mkz_msgs/ParkingBrake";
  }

  static const char* value(const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 status\n"
"\n"
"uint8 OFF=0\n"
"uint8 TRANS=1\n"
"uint8 ON=2\n"
"uint8 FAULT=3\n"
;
  }

  static const char* value(const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.status);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ParkingBrake_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dbw_mkz_msgs::ParkingBrake_<ContainerAllocator>& v)
  {
    s << indent << "status: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.status);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DBW_MKZ_MSGS_MESSAGE_PARKINGBRAKE_H
