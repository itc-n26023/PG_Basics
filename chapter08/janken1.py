import random

def play_janken():
    # 手の定義
    hands = {1: "✊", 2: "✌", 3: "✋"}
    
    print("--- じゃんけんゲーム ---")
    print("1: ✊, 2: ✌, 3: ✋")
    
    # プレイヤーの入力処理
    try:
        player_choice = int(input("あなたの手を選んでください (1-3): "))
        if player_choice not in hands:
            print("無効な数字です。1, 2, 3 のいずれかを入力してください。")
            return
    except ValueError:
        print("数字を入力してください。")
        return

    # コンピュータの手をランダムに決定
    computer_choice = random.randint(1, 3)

    # 結果の表示
    print(f"\nあなたの手: {hands[player_choice]}")
    print(f"相手の手 : {hands[computer_choice]}")
    print("-----------------------")

    # 勝敗の判定
    if player_choice == computer_choice:
        print("結果: あいこ👊")
    elif (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 3) or \
         (player_choice == 3 and computer_choice == 1):
        print("結果: 勝ち！ 🎉")
    else:
        print("結果: 負け... 😢")

if __name__ == "__main__":
    play_janken()
