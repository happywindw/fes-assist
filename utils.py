# -*- coding: utf-8 -*-
import winreg
import paramiko
from feslogs import FesLogger
from settings import sftp_ser

logger = FesLogger().get_logger()


def insert_into_gird(grid, data, row_labels=None, col_labels=None):
    """
    将一个多维数组展示在一个wxgird表格当中。表格大小会根据数据格式自动伸缩。
    :param grid:
    :param data:
    :param row_labels:
    :param col_labels:
    :return:
    """
    if not len(data):
        return
    row_num, col_num = len(data), len(data[0])
    grid_row_num = grid.GetNumberRows()
    grid_col_num = grid.GetNumberCols()

    # 设置行数与列数使之与数据匹配
    if row_num > grid_row_num:
        grid.AppendRows(row_num - grid_row_num)
    if row_num < grid_row_num:
        grid.DeleteRows(row_num, grid_row_num - row_num)
    if col_num > grid_col_num:
        grid.AppendCols(col_num - grid_col_num)
    if col_num < grid_col_num:
        grid.DeleteCols(col_num, grid_col_num - col_num)

    # 设置各行、列的标题
    if row_labels and len(row_labels) == row_num:
        for i, lab in enumerate(row_labels):
            grid.SetRowLabelValue(i, lab)
    if col_labels and len(col_labels) == col_num:
        for j, lab in enumerate(col_labels):
            grid.SetColLabelValue(j, lab)

    # 填充数据
    for j, row in enumerate(data):
        for i, ele in enumerate(row):
            grid.SetCellValue(j, i, str(ele))
    grid.AutoSize()


def sftp_download(remote, local):
    sf = paramiko.Transport((sftp_ser['host'], sftp_ser['port']))
    sf.connect(username=sftp_ser['username'], password=sftp_ser['password'])
    sftp = paramiko.SFTPClient.from_transport(sf)
    flag = False
    try:
        logger.info('Start to download remote file: [%s]%s' % (sftp_ser['host'], remote))
        sftp.get(remote, local)  # 下载文件
        logger.info('Success download file: %s' % local)
        flag = True
    except Exception as e:
        logger.error('Download exception:' % e)
    sf.close()
    return flag


def get_desktop():
    """
    获取windows系统桌面路径
    :return:
    """
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]
