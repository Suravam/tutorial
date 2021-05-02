mac = [0, 0, 0, 0, 0, 0]
def generateMAC(index):
    if index < 0:
        return
    else:
        generateMAC(index - 1)
    while mac[index] < 255:
        mac[index] = mac[index] + 1
        yield ':'.join(map(lambda x: "%02x" % x, mac))
        generateMAC(index - 1)
    mac[index] = 0