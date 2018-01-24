def trap(heights):
    """
    :type height: List[int]
    :rtype: int
    """
    last_big_bar = 0
    fill_flag = False
    big_count = 0
    small_count = 0
    for curr_bar in heights:
        if fill_flag:
            if(curr_bar <= last_big_bar):
                small_count = small_count + last_big_bar - curr_bar
            else:
                # curr_bar is higher than last_big_bar
                last_big_bar = curr_bar
                fill_flag = False
        else:
            if curr_bar <= last_big_bar:
                fill_flag = True
            else:
                fill_flag = False
    return small_count



print trap([0,1,0,2,1,0,1,3,2,1,2,1])