

"""
 HuskyLens API Guide
"""
HUSKYLENS_APIS = [

  _("huskylens.command_knock() \nConnection initialization"),#连接初始化
  _("huskylens.command_algorthim(algorthim) \nselection algorithm 'ALGORITHM_FACE_RECOGNITION' 'ALGORITHM_OBJECT_TRACKING' 'ALGORITHM_OBJECT_RECOGNITION' 'ALGORITHM_LINE_TRACKING' 'ALGORITHM_COLOR_RECOGNITION' 'ALGORITHM_TAG_RECOGNITION' 'ALGORITHM_OBJECT_CLASSIFICATION' "),#选择算法
  _("huskylens.command_request() \nGet huskylens raw data"),#获取哈士奇原始数据
  _("huskylens.command_request_learn_once(id) \nAutomatic learning ID "),#自动学习ID
  _("huskylens.command_request_forget() \nForgetting the current algorithm"),#遗忘当前算法
  _("huskylens.command_request_customnames(id, name) \nModify ID name"),#修改ID名称
  _("huskylens.command_request_custom_text(test, x, y) \nDisplay text in the specified position on the screen"),#在屏幕指定位置显示文字
  _("huskylens.command_request_clear_text() \nClear screen text"),#清除屏幕文字
  _("huskylens.command_request_save_mode_to_SD_card(index) \nSave the current algorithm to the SD card index number model"),#保存当前算法到SD卡index号模型
  _("huskylens.command_request_load_model_from_SD_card() \nLoading index model from SD card"),#从SD卡加载index号模型
  _("huskylens.command_request_photo() \nSave photos to SD card"),#保存照片到SD卡
  _("huskylens.command_request_screenshot() \nSave screenshot to SD card")#保存截图到SD卡
]
