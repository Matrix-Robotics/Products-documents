#ifndef SMART_CAM_READER_H  // 防止头文件重复包含
#define SMART_CAM_READER_H

#include <Arduino.h>

// 函数声明
int SmartCamReader(unsigned int *data, unsigned int timeout = 500);  // timeout设置默认值为500ms

#endif
