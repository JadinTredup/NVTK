def parse_eeg_data(sample, channel, aux):
    id_str = str(sample_id) + ', '
    channel_str = ''
    for i in channel:
        channel_str = channel_str + str(i)[:-9] + ", "

    aux_str = ''
    for i in aux:
        aux_str = aux_str + str(i) + ', '

    data_str = id_str + channel_str + aux_str + '\n'
    return data_str