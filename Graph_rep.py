raw = [2.1466, 2.1843, 2.0942, 2.0587, 2.0836, 2.3328, 2.4024,
       2.4547, 2.4201, 2.3994, 2.4200, 2.2712, 2.3731, 2.2722]

gain = sum(max(raw[i] - raw[i - 1], 0) for i in range(1, len(raw))) / 14
loss = sum(max(raw[i - 1] - raw[i], 0) for i in range(1, len(raw))) / 14

RS = gain / loss
RSI = 100 - (100 / (1 + RS))

print("Gain:", gain, "Loss:", loss, "RS:", RS, "RSI:", RSI)
print("Gain:", gain, "Loss:", loss)
print("RS:", RS)
original = 100
