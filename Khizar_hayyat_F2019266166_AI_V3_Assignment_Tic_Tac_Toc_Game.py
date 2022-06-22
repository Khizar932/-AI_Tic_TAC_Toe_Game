

if __name__ == '__main__':
    # A Python program to print all
    # permutations of given length
    from itertools import permutations

    # Get all permutations of length 2
    # and length 2
    perm = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8], 9))



    def chk_user(board):
        d = 0


        user_ = board[::2]
        user_idx = 0
        dummy_user = []
        # print('user', user)
        # print('cmp', cmp)
        ls = False
        flag = True
        for i in range(0, len(board)):
            d = d + 1
            if user_idx < len(user_):
                dummy_user.append(user_[user_idx])
                user_idx += 1
            # if count_user < 4:

            # print('dumy user', dummy_user)
            if check_for_win(dummy_user):
                # win = win + 1
                ls = True
                flag = False
        return ls

    def chk_cmp(board):
        cmp_ = board[1::2]
        cmp_idx = 0
        dummy_cmp = []
        # print('user', user)
        # print('cmp', cmp)
        ls = False
        flag = True
        for i in range(0, len(board)):
            if cmp_idx < len(cmp_):
                dummy_cmp.append(cmp_[cmp_idx])
                cmp_idx += 1


            if check_for_win(dummy_cmp):
                # win = win + 1
                ls = True
                flag = False

        return ls

    def check_for_win(val):
        dummy = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        for i in val:

            dummy[i] = 'x'

        # 0 1 2
        # 3 4 5
        # 6 7 8
        if dummy[0] == 'x' and dummy[1] == 'x' and dummy[2] == 'x':
            for k, v in enumerate(dummy):
                dummy[k] = '-'
            return True

        if dummy[3] == 'x' and dummy[4] == 'x' and dummy[5] == 'x':
            for k, v in enumerate(dummy):
                dummy[k] = '-'
            return True

        if dummy[6] == 'x' and dummy[7] == 'x' and dummy[8] == 'x':
            for k, v in enumerate(dummy):
                dummy[k] = '-'
            return True

        if dummy[0] == 'x' and dummy[3] == 'x' and dummy[6] == 'x':
            for k, v in enumerate(dummy):
                dummy[k] = '-'
            return True

        if dummy[1] == 'x' and dummy[4] == 'x' and dummy[7] == 'x':
            for k, v in enumerate(dummy):
                dummy[k] = '-'
            return True

        if dummy[2] == 'x'  and dummy[5] == 'x' and dummy[8] == 'x' :
            for k, v in enumerate(dummy):
                dummy[k] = '-'
            return True

        if dummy[0] == 'x' and dummy[4] == 'x' and dummy[8] == 'x' :
            for k, v in enumerate(dummy):
                dummy[k] = '-'
            return True

        if dummy[2] == 'x'  and dummy[4] == 'x' and dummy[6] == 'x':
            for k, v in enumerate(dummy):
                dummy[k] = '-'
            return True

        return False

        # ----------------------------------------------------------------------


    def score(tp):
        d = 0
        user = tp[::2]
        cmp = tp[1::2]
        dummy_user = []
        dummy_cmp = []
        # print('user', user)
        # print('cmp', cmp)
        cmp_idx = 0
        user_idx = 0
        ls = True
        flag = True
        for i in range(0, len(tp)):
            d = d + 1
            if cmp_idx < len(cmp):
                dummy_cmp.append(cmp[cmp_idx])
                cmp_idx += 1
            # if count_user < 4:
            if user_idx < len(user):
                dummy_user.append(user[user_idx])
                user_idx += 1
            # count_user = count_user + 1
            if check_for_win(dummy_user):
                # lose += 1
                ls = False
                flag = False

            if check_for_win(dummy_cmp):
                # win = win + 1
                ls = True
                flag = False

            if not check_for_win(dummy_user) and not check_for_win(dummy_cmp):
                # tie = tie + 1
                ls = 'tie'

                flag = False
        return ls



    user = []
    cmp = []
    options = [0, 1, 2, 3, 4, 5, 6, 7, 8]


    def comp_move(win_lose, possible):
        ls = win_lose[possible[0]]['lose']
        i_l = possible[0]
        print(ls, i_l)
        for key, value in win_lose.items():
            if value['lose'] < ls:
                ls = value['lose']
                i_l = key

        print('I*L', i_l)
        return i_l


    def update_possible(l1, l2):
        s = list(set(l1) - set(l2)) + list(set(l2) - set(l1))
        # print(s)
        return s

    def symbol(tp_user, tp_cmp, pos):
        sm = 'x' # for computer
        # print(tp_cmp, tp_user)
        if pos in tp_cmp:
            return sm
        elif pos in tp_user:
            sm = 'U'
            return sm
        else:
            sm = str(pos)
            return sm

    def print_board(board):
        user = board[::2]
        cmp = board[1::2]
        print(f''' 
                {symbol(user, cmp, 0)}    |   {symbol(user, cmp, 1)}   |   {symbol(user, cmp, 2)}   
                -----------------
                {symbol(user, cmp, 3)}    |   {symbol(user, cmp, 4)}   |   {symbol(user, cmp, 5)}
                -----------------
                {symbol(user, cmp, 6)}    |   {symbol(user, cmp, 7)}   |   {symbol(user, cmp, 8)}''')


    print('=======================================================')
    print('X == user')
    print('U = user')
    print('=======================================================')
    ur = int(input('User Turn Please Enter a Value :  '))

    board = []
    board.append(ur)
    possible = options.copy()
    possible.remove(ur)
    # print(possible)
    new_perm = []
    scr = []
    # print(board)


    while len(board) != 9:
        win, lose, tie = 0, 0, 0
        win_lose_tie = {}
        for i in range(0, len(perm)):
            l = perm[i]
            if list(l[0:len(board)]) == board:
                new_perm.append(l)

        mex = possible[0]
        # print(len(possible))
        c = 0
        while len(possible) != 0:
            board.append(possible.pop(0))
            for i in range(0, len(new_perm)):
                l = new_perm[i]
                if list(l[0: len(board)]) == board:
                    if score(l) == True:
                        win += 1
                    if score(l) == False:
                        lose += 1
                    if score(l) == 'tie':
                        tie += 1

            # print('kkkkkkkkkkkkkkkk')
            win_lose_tie[board.pop()] = {'win': win, 'lose': lose, 'tie': tie}
            win, lose, tie = 0, 0, 0

        # print(possible, board)

        possible = options.copy()
        possible = update_possible(possible, board)
        # print(possible, 'CMP T POSSIBLE')
        print(win_lose_tie)
        cmp_mv = comp_move(win_lose_tie, possible)
        board.append(cmp_mv)
        print(board, 'CMP TURN BOARD')
        print_board(board)

        possible = options.copy()
        possible = update_possible(possible, board)

        if len(board) > 5:
            ck_user = chk_user(board)
            ck_cmp = chk_cmp(board)

            # print(ck_cmp, ck_user)

            # print('9999999999999999999999999999999')

            if ck_user:
                print('**********  User Win   ************')
                break
            if chk_cmp(board):
                print('**********  Computer Win   ************')
                break
        print(f'From : {possible}')
        inputValue = int(input("please select one:"))
        while inputValue not in possible:
            inputValue = int(input("please select again: "))
        board.append(inputValue)
        if len(board) > 5:
            ck_user = chk_user(board)
            ck_cmp = chk_cmp(board)

            if ck_user:
                print('**********  User Win   ************')
                break
            if ck_cmp:
                print('**********  Computer Win   ************')
                break
        possible = options.copy()
        possible = update_possible(possible, board)
        # print(possible, "POssible")
        # print(board, 'BOARD')
        new_perm.clear()















