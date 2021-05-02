def f_generateMAC(index):
    if index < 0:
        return
    else:
        generateMAC(index - 1)
    while mac[index] < 255:
        macs.append(':'.join(map(lambda x: "%02x" % x, mac)))
        mac[index] = mac[index] + 1
        generateMAC(index - 1)
    mac[index] = 0
    return macs