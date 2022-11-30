import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

plt.style.use('ggplot')

"""
def gsf_read(file_name):
    if file_name.rpartition(".")[1] == ".":
        file_name = file_name[0 : file_name.rfind(".")]

    gsfFile = open(file_name + ".gsf", "rb")

    metadata = {}

    # check if header is OK
    if not (gsfFile.readline().decode("UTF-8") == "Gwyddion Simple Field 1.0\n"):
        gsfFile.close()
        raise ValueError("File has wrong header")

    term = b"00"
    # read metadata header
    while term != b"\x00":
        line_string = gsfFile.readline().decode("UTF-8")
        metadata[line_string.rpartition(" = ")[0]] = line_string.rpartition("=")[2]
        term = gsfFile.read(1)
        gsfFile.seek(-1, 1)

    gsfFile.read(4 - gsfFile.tell() % 4)

    # fix known metadata types from .gsf file specs
    # first the mandatory ones...
    metadata["XRes"] = np.int32(metadata["XRes"])
    metadata["YRes"] = np.int32(metadata["YRes"])

    # now check for the optional ones
    if "XReal" in metadata:
        metadata["XReal"] = np.float64(metadata["XReal"])

    if "YReal" in metadata:
        metadata["YReal"] = np.float64(metadata["YReal"])

    if "XOffset" in metadata:
        metadata["XOffset"] = np.float(metadata["XOffset"])

    if "YOffset" in metadata:
        metadata["YOffset"] = np.float(metadata["YOffset"])

    data = np.frombuffer(gsfFile.read(), dtype="float32").reshape(
        metadata["YRes"], metadata["XRes"]
    )

    gsfFile.close()

    return metadata, data


(meta, data) = gsf_read("2022.09.21_0a-2.gsf")

np.savetxt("2022.09.21_0a-2.txt", data, delimiter=",")
plt.imshow(data)
plt.show()
"""