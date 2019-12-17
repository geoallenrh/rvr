#!/usr/bin/env python3
# This file is automatically generated!
# Source File:        0x18-sensors.json
# Device ID:          0x18
# Device Name:        sensor
# Timestamp:          10/12/2019 @ 01:43:14.086610 (UTC)

from sphero_sdk.common.enums.sensor_enums import CommandsEnum
from sphero_sdk.common.devices import DevicesEnum
from sphero_sdk.common.parameter import Parameter
from sphero_sdk.common.sequence_number_generator import SequenceNumberGenerator


def enable_gyro_max_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_gyro_max_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def on_gyro_max_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.gyro_max_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='flags',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def reset_locator_x_and_y(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.reset_locator_x_and_y,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def set_locator_flags(flags, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.set_locator_flags,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='flags',
                data_type='uint8_t',
                index=0,
                value=flags,
                size=1
            ),
        ],
    }


def get_bot_to_bot_infrared_readings(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_bot_to_bot_infrared_readings,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='sensorData',
                data_type='uint32_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_rgbc_sensor_values(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_rgbc_sensor_values,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='redChannelValue',
                data_type='uint16_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='greenChannelValue',
                data_type='uint16_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='blueChannelValue',
                data_type='uint16_t',
                index=2,
                size=1,
            ),
            Parameter( 
                name='clearChannelValue',
                data_type='uint16_t',
                index=3,
                size=1,
            ),
        ]
    }


def start_robot_to_robot_infrared_broadcasting(far_code, near_code, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.start_robot_to_robot_infrared_broadcasting,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='farCode',
                data_type='uint8_t',
                index=0,
                value=far_code,
                size=1
            ),
            Parameter( 
                name='nearCode',
                data_type='uint8_t',
                index=1,
                value=near_code,
                size=1
            ),
        ],
    }


def start_robot_to_robot_infrared_following(far_code, near_code, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.start_robot_to_robot_infrared_following,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='farCode',
                data_type='uint8_t',
                index=0,
                value=far_code,
                size=1
            ),
            Parameter( 
                name='nearCode',
                data_type='uint8_t',
                index=1,
                value=near_code,
                size=1
            ),
        ],
    }


def stop_robot_to_robot_infrared_broadcasting(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.stop_robot_to_robot_infrared_broadcasting,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def on_robot_to_robot_infrared_message_received_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.robot_to_robot_infrared_message_received_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='infraredCode',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
        ]
    }


def get_ambient_light_sensor_value(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_ambient_light_sensor_value,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='ambientLightValue',
                data_type='float',
                index=0,
                size=1,
            ),
        ]
    }


def stop_robot_to_robot_infrared_following(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.stop_robot_to_robot_infrared_following,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def start_robot_to_robot_infrared_evading(far_code, near_code, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.start_robot_to_robot_infrared_evading,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='farCode',
                data_type='uint8_t',
                index=0,
                value=far_code,
                size=1
            ),
            Parameter( 
                name='nearCode',
                data_type='uint8_t',
                index=1,
                value=near_code,
                size=1
            ),
        ],
    }


def stop_robot_to_robot_infrared_evading(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.stop_robot_to_robot_infrared_evading,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def enable_color_detection_notify(is_enabled, interval, minimum_confidence_threshold, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_color_detection_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
            Parameter( 
                name='interval',
                data_type='uint16_t',
                index=1,
                value=interval,
                size=1
            ),
            Parameter( 
                name='minimumConfidenceThreshold',
                data_type='uint8_t',
                index=2,
                value=minimum_confidence_threshold,
                size=1
            ),
        ],
    }


def on_color_detection_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.color_detection_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='red',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='green',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='blue',
                data_type='uint8_t',
                index=2,
                size=1,
            ),
            Parameter( 
                name='confidence',
                data_type='uint8_t',
                index=3,
                size=1,
            ),
            Parameter( 
                name='colorClassificationId',
                data_type='uint8_t',
                index=4,
                size=1,
            ),
        ]
    }


def get_current_detected_color_reading(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_current_detected_color_reading,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def enable_color_detection(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_color_detection,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def configure_streaming_service(token, configuration, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.configure_streaming_service,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='token',
                data_type='uint8_t',
                index=0,
                value=token,
                size=1
            ),
            Parameter( 
                name='configuration',
                data_type='uint8_t',
                index=1,
                value=configuration,
                size=15
            ),
        ],
    }


def start_streaming_service(period, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.start_streaming_service,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='period',
                data_type='uint16_t',
                index=0,
                value=period,
                size=1
            ),
        ],
    }


def stop_streaming_service(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.stop_streaming_service,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def clear_streaming_service(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.clear_streaming_service,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
    }


def on_streaming_service_data_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.streaming_service_data_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='token',
                data_type='uint8_t',
                index=0,
                size=1,
            ),
            Parameter( 
                name='sensorData',
                data_type='uint8_t',
                index=1,
                size=9999,
            ),
        ]
    }


def enable_robot_infrared_message_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_robot_infrared_message_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def send_infrared_message(infrared_code, front_strength, left_strength, right_strength, rear_strength, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.send_infrared_message,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='infraredCode',
                data_type='uint8_t',
                index=0,
                value=infrared_code,
                size=1
            ),
            Parameter( 
                name='frontStrength',
                data_type='uint8_t',
                index=1,
                value=front_strength,
                size=1
            ),
            Parameter( 
                name='leftStrength',
                data_type='uint8_t',
                index=2,
                value=left_strength,
                size=1
            ),
            Parameter( 
                name='rightStrength',
                data_type='uint8_t',
                index=3,
                value=right_strength,
                size=1
            ),
            Parameter( 
                name='rearStrength',
                data_type='uint8_t',
                index=4,
                value=rear_strength,
                size=1
            ),
        ],
    }


def get_motor_temperature(motor_index, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_motor_temperature,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='motorIndex',
                data_type='uint8_t',
                index=0,
                value=motor_index,
                size=1
            ),
        ],
        'outputs': [ 
            Parameter( 
                name='windingCoilTemperature',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter( 
                name='caseTemperature',
                data_type='float',
                index=1,
                size=1,
            ),
        ]
    }


def get_motor_thermal_protection_status(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.get_motor_thermal_protection_status,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='leftMotorTemperature',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter( 
                name='leftMotorStatus',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='rightMotorTemperature',
                data_type='float',
                index=2,
                size=1,
            ),
            Parameter( 
                name='rightMotorStatus',
                data_type='uint8_t',
                index=3,
                size=1,
            ),
        ]
    }


def enable_motor_thermal_protection_status_notify(is_enabled, target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.enable_motor_thermal_protection_status_notify,
        'seq': SequenceNumberGenerator.get_sequence_number(),
        'target': target,
        'timeout': timeout,
        'inputs': [ 
            Parameter( 
                name='isEnabled',
                data_type='bool',
                index=0,
                value=is_enabled,
                size=1
            ),
        ],
    }


def on_motor_thermal_protection_status_notify(target, timeout): 
    return { 
        'did': DevicesEnum.sensor,
        'cid': CommandsEnum.motor_thermal_protection_status_notify,
        'target': target,
        'timeout': timeout,
        'outputs': [ 
            Parameter( 
                name='leftMotorTemperature',
                data_type='float',
                index=0,
                size=1,
            ),
            Parameter( 
                name='leftMotorStatus',
                data_type='uint8_t',
                index=1,
                size=1,
            ),
            Parameter( 
                name='rightMotorTemperature',
                data_type='float',
                index=2,
                size=1,
            ),
            Parameter( 
                name='rightMotorStatus',
                data_type='uint8_t',
                index=3,
                size=1,
            ),
        ]
    }