import numpy as np

# class StringToMatrix:
def strings_to_matrix_calculation(str1):
    try:
        f, s = "", ""
        f_s, t_s, s_s, w0_s, w1_s, w2_s, w3_s = 0, 0, 0, 0, 0, 0, 0
        str_len = len(str1)
        w = [None]*4
        i = 0
        if str_len > 1:
            f, s = str1[0:int(len(str1) // 2)], str1[int(len(str1) // 2):]
            if 1 < len(f) < 3:
                f, w[0] = f[0:int(len(f) // 2)], f[int(len(f) // 2):]
                i = i + 1
            elif int(len(f)) > 2:
                f, w[i], w[i + 1] = f[0:int(len(f) // 3)], f[int(len(f)//3): int(2 * len(f) // 3)], f[int(2 * (len(f) //
                                                                                                            3)):]
                i = i + 2
            elif f and int(len(f)) == 1:
                pass
            if 1 < int(len(s)) < 3:
                s, w[i] = s[0:int(len(s) // 2)], s[int((len(s) // 2)):]
                i = i + 1
            elif len(s) > 2:
                s, w[i], w[i + 1] = s[0:int(len(s) // 3)], s[int(len(s)//3): int(2 * len(s) // 3)], s[int(2 * (len(s) //
                                                                                                            3)):]
                i = i + 2
            elif s and int(len(s)) == 1:
                pass
        if str_len > 1:
            str1 = str1.encode('ascii')
            arr = np.frombuffer(str1, dtype=np.uint8)
            data_arr = np.array(arr)
            t_s = int(np.sum(data_arr))
            arr = np.frombuffer(f.encode('ascii'), dtype=np.uint8)
            data_arr = np.array(arr)
            f_s = int(np.sum(data_arr))
            arr = np.frombuffer(s.encode('ascii'), dtype=np.uint8)
            data_arr = np.array(arr)
            s_s = int(np.sum(data_arr))
            if w[0]:
                arr = np.frombuffer(w[0].encode('ascii'), dtype=np.uint8)
                data_arr = np.array(arr)
                w0_s = int(np.sum(data_arr))
            if w[1]:
                arr = np.frombuffer(w[1].encode('ascii'), dtype=np.uint8)
                data_arr = np.array(arr)
                w1_s = int(np.sum(data_arr))
            if w[2]:
                arr = np.frombuffer(w[2].encode('ascii'), dtype=np.uint8)
                data_arr = np.array(arr)
                w2_s = int(np.sum(data_arr))
            if w[3]:
                arr = np.frombuffer(w[3].encode('ascii'), dtype=np.uint8)
                data_arr = np.array(arr)
                w3_s = int(np.sum(data_arr))
        else:
            arr = np.frombuffer(str1.encode('ascii'), dtype=np.uint8)
            data_arr = np.array(arr)
            t_s = int(np.sum(data_arr))
        # print(f)
        # print(s)
        # print(w[0])
        # print(w[1])
        # print(w[2])
        # print(w[3])
        if str_len > 1 and w[0] is None and w[1] is None and w[2] is None and w[3] is None:
            word_lst = [f_s, s_s]
        elif str_len > 1 and w[0] is not None and w[1] is None and w[2] is None and w[3] is None:
            word_lst = [f_s, s_s, w0_s]
        elif str_len > 1 and w[0] is not None and w[1] is not None and w[2] is None and w[3] is None:
            word_lst = [f_s, s_s, w0_s, w1_s]
        elif str_len > 1 and w[0] is not None and w[1] is not None and w[2] is not None and w[3] is None:
            word_lst = [f_s, s_s, w0_s, w1_s, w2_s]
        elif str_len > 1 and w[0] is not None and w[1] is not None and w[2] is not None and w[3] is not None:
            word_lst = [f_s, s_s, w0_s, w1_s, w2_s, w3_s]
        else:
            word_lst = [t_s, str_len]
        return word_lst
    except Exception as e:
        raise(e)


# if __name__ == "__main__":
#     """w_lst = strings_to_matrix_calculation("testerfor")
#     print(w_lst)
#     t_lst = strings_to_matrix_calculation("tasterfor")
#     print(w_lst[2])
#     #   print(np.matrix(w_lst[2]))
#     #   print(np.matrix(t_lst[2]))
#     res = np.subtract(np.matrix(w_lst[2]), np.matrix(t_lst[2]))
#     print(res)
#     """
#     print(int(10/2))
#     print(int((10/2)/3))

