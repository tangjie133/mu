from microbit import *
import microbit
import struct
import utime

algorthims_byteID = {
  "ALGORITHM_FACE_RECOGNITION": "0000",
  "ALGORITHM_OBJECT_TRACKING": "0100",
  "ALGORITHM_OBJECT_RECOGNITION": "0200",
  "ALGORITHM_LINE_TRACKING": "0300",
  "ALGORITHM_COLOR_RECOGNITION": "0400",
  "ALGORITHM_TAG_RECOGNITION": "0500",
  "ALGORITHM_OBJECT_CLASSIFICATION": "0600"
}

class Huskylens:
    command_header = "55AA11"
    def __init__(self,i2caddr = 0x32):
        self.I2C = microbit.i2c
        self.I2C.init(freq=100000,sda=pin20,scl=pin19)


    def _write_to_huskylens(self, cmd):
        buf = bytearray(len(cmd)//2)
        for i in range(len(cmd)//2):
            buf[i] = int(cmd[i*2 : i*2 + 2], 16)
        self.I2C.write(0x32, buf)

    def _calculate_checksum(self, hexStr):
        total = 0
        for i in range(0, len(hexStr), 2):
            total += int(hexStr[i:i+2], 16)
        hexStr = hex(total)[-2:]
       	return hexStr

    def _split_command_to_parts(self, dataArray):
            headers = dataArray[0:2]
            address = dataArray[2]
            data_length = dataArray[3]
            command = dataArray[4]
            if(data_length > 0):
                data = dataArray[5:-2]
            else:
                data = []
            checkSum = dataArray[-1]
            return [headers, address, data_length, command, data, checkSum]

    def _process_return_data(self):
        resonse_data = self._read_response()
        parsed_data = self._parse_response(resonse_data)
        return self._data_process(parsed_data)

    def _read_response(self):
        x = 0
        resonse_data = []
        keep_reading = True
        while keep_reading:
            d = struct.unpack('b', self.I2C.read(0x32, 1))
            if(d[0] == 0x55):
                resonse_data.append(d[0])
                tmp = []
                for i in range(15):
                    tmp = struct.unpack('b', self.I2C.read(0x32, 1))
                    utime.sleep_ms(10)
                    resonse_data.append(tmp[0])
                    tmp = []
                keep_reading = False
        return resonse_data

    def _parse_response(self, resonse_data):
        command_split = self._split_command_to_parts(resonse_data)
        return_data = []
        if(command_split[3] == 0x2e):
            return "KNOCK RECEIVED"
        else:
            number_of_block_or_arrow = command_split[4][0]
            if(command_split[4][1] > 0):
                number_of_block_or_arrow = 255 + command_split[4][1]
            for i in range(number_of_block_or_arrow):
                block_or_arrow_resp = self._read_response()
                split_into_pates = self._split_command_to_parts(block_or_arrow_resp)
                return_data.append(split_into_pates[4])
        return return_data

    def _data_process(self, return_data):
        if(return_data != "KNOCK RECEIVED"):
            data = []
            for index,q in enumerate(return_data):
                for i in range(0, len(q)-1, 2):
                    val = q[i]
                    if(q[i+1]>0):
                        val = 255 + q[i+1]
                    data.append(val)
                data.append(q[-1])
            return data

    def command_knock(self):
        cmd = Huskylens.command_header+"002c"
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)
        return self._process_return_data()

    def command_algorthim(self,alg):
        if alg in algorthims_byteID:
                cmd = Huskylens.command_header + "022d" + algorthims_byteID[alg]
                cmd += self._calculate_checksum(cmd)
                self._write_to_huskylens(cmd)
                return self._process_return_data()
        else:
            print('INCORRECT ALGORITHIM NAME')

    def command_request(self):
        cmd = Huskylens.command_header+"0020"
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)
        return self._process_return_data()

    def command_request_learn_once(self, id):
        data = "{:04x}".format(id)
        part1=data[2:]
        part2=data[0:2]
        data=part1+part2
        cmd = Huskylens.command_header + "0236" + data
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

    def command_request_forget(self):
        cmd = cmd = Huskylens.command_header+"0037"
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

    def command_request_customnames(self, id, name):
        data = "{:02x}".format(id)
        name_data = ""
        for i in range(len(name)):
            name_data += "{:02x}".format(ord(name[i:i+1]))
        name_data_size = "{:02x}".format((len(name)+1)*2)
        data_length = "{:02x}".format((len(name))+3)
        cmd = Huskylens.command_header + data_length + "2f" + data + name_data_size + name_data + "00"
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

    def command_request_custom_test(self, text,x,y):
        if (x>255):
            x = "ff"+"{:02x}".format(x%255)
        else:
            x= "00"+"{:02x}".format(x)
        y="{:02x}".format(y)
        data = x + y

        data_length = "{:02x}".format((len(text))+4)
        text_data = ""
        for i in range(len(text)):
            text_data += "{:02x}".format(ord(text[i:i+1]))
        text_data_size = "{:02x}".format(len(text))
        cmd = Huskylens.command_header + data_length + "34" + text_data_size + data + text_data
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

    def command_request_clear_text(self):
        cmd = cmd = Huskylens.command_header+"0035"
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

    def command_request_save_mode_to_SD_card(self, index):
        data = "{:04x}".format(index)
        part1=data[2:]
        part2=data[0:2]
        data=part1+part2
        cmd = Huskylens.command_header + "0232" + data
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

    def command_request_load_model_from_SD_card(self, index):
        data = "{:04x}".format(index)
        part1=data[2:]
        part2=data[0:2]
        data=part1+part2
        cmd = Huskylens.command_header + "0233" + data
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

    def command_request_photo(self):
        cmd = Huskylens.command_header+"0030"
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

    def command_request_screenshot(self):
        cmd = Huskylens.command_header+"0039"
        cmd += self._calculate_checksum(cmd)
        self._write_to_huskylens(cmd)

