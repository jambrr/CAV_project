// Generated by gencpp from file dbw_mkz_msgs/Wiper.msg
// DO NOT EDIT!


#ifndef DBW_MKZ_MSGS_MESSAGE_WIPER_H
#define DBW_MKZ_MSGS_MESSAGE_WIPER_H


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
struct Wiper_
{
  typedef Wiper_<ContainerAllocator> Type;

  Wiper_()
    : status(0)  {
    }
  Wiper_(const ContainerAllocator& _alloc)
    : status(0)  {
  (void)_alloc;
    }



   typedef uint8_t _status_type;
  _status_type status;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(OFF)
  #undef OFF
#endif
#if defined(_WIN32) && defined(AUTO_OFF)
  #undef AUTO_OFF
#endif
#if defined(_WIN32) && defined(OFF_MOVING)
  #undef OFF_MOVING
#endif
#if defined(_WIN32) && defined(MANUAL_OFF)
  #undef MANUAL_OFF
#endif
#if defined(_WIN32) && defined(MANUAL_ON)
  #undef MANUAL_ON
#endif
#if defined(_WIN32) && defined(MANUAL_LOW)
  #undef MANUAL_LOW
#endif
#if defined(_WIN32) && defined(MANUAL_HIGH)
  #undef MANUAL_HIGH
#endif
#if defined(_WIN32) && defined(MIST_FLICK)
  #undef MIST_FLICK
#endif
#if defined(_WIN32) && defined(WASH)
  #undef WASH
#endif
#if defined(_WIN32) && defined(AUTO_LOW)
  #undef AUTO_LOW
#endif
#if defined(_WIN32) && defined(AUTO_HIGH)
  #undef AUTO_HIGH
#endif
#if defined(_WIN32) && defined(COURTESYWIPE)
  #undef COURTESYWIPE
#endif
#if defined(_WIN32) && defined(AUTO_ADJUST)
  #undef AUTO_ADJUST
#endif
#if defined(_WIN32) && defined(RESERVED)
  #undef RESERVED
#endif
#if defined(_WIN32) && defined(STALLED)
  #undef STALLED
#endif
#if defined(_WIN32) && defined(NO_DATA)
  #undef NO_DATA
#endif

  enum {
    OFF = 0u,
    AUTO_OFF = 1u,
    OFF_MOVING = 2u,
    MANUAL_OFF = 3u,
    MANUAL_ON = 4u,
    MANUAL_LOW = 5u,
    MANUAL_HIGH = 6u,
    MIST_FLICK = 7u,
    WASH = 8u,
    AUTO_LOW = 9u,
    AUTO_HIGH = 10u,
    COURTESYWIPE = 11u,
    AUTO_ADJUST = 12u,
    RESERVED = 13u,
    STALLED = 14u,
    NO_DATA = 15u,
  };


  typedef boost::shared_ptr< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> const> ConstPtr;

}; // struct Wiper_

typedef ::dbw_mkz_msgs::Wiper_<std::allocator<void> > Wiper;

typedef boost::shared_ptr< ::dbw_mkz_msgs::Wiper > WiperPtr;
typedef boost::shared_ptr< ::dbw_mkz_msgs::Wiper const> WiperConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dbw_mkz_msgs::Wiper_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dbw_mkz_msgs::Wiper_<ContainerAllocator1> & lhs, const ::dbw_mkz_msgs::Wiper_<ContainerAllocator2> & rhs)
{
  return lhs.status == rhs.status;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dbw_mkz_msgs::Wiper_<ContainerAllocator1> & lhs, const ::dbw_mkz_msgs::Wiper_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dbw_mkz_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7fccb48d5d1df108afaa89f8fc14ce1c";
  }

  static const char* value(const ::dbw_mkz_msgs::Wiper_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7fccb48d5d1df108ULL;
  static const uint64_t static_value2 = 0xafaa89f8fc14ce1cULL;
};

template<class ContainerAllocator>
struct DataType< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dbw_mkz_msgs/Wiper";
  }

  static const char* value(const ::dbw_mkz_msgs::Wiper_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 status\n"
"\n"
"uint8 OFF=0\n"
"uint8 AUTO_OFF=1\n"
"uint8 OFF_MOVING=2\n"
"uint8 MANUAL_OFF=3\n"
"uint8 MANUAL_ON=4\n"
"uint8 MANUAL_LOW=5\n"
"uint8 MANUAL_HIGH=6\n"
"uint8 MIST_FLICK=7\n"
"uint8 WASH=8\n"
"uint8 AUTO_LOW=9\n"
"uint8 AUTO_HIGH=10\n"
"uint8 COURTESYWIPE=11\n"
"uint8 AUTO_ADJUST=12\n"
"uint8 RESERVED=13\n"
"uint8 STALLED=14\n"
"uint8 NO_DATA=15\n"
;
  }

  static const char* value(const ::dbw_mkz_msgs::Wiper_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.status);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Wiper_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dbw_mkz_msgs::Wiper_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dbw_mkz_msgs::Wiper_<ContainerAllocator>& v)
  {
    s << indent << "status: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.status);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DBW_MKZ_MSGS_MESSAGE_WIPER_H
