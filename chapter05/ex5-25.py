# 19世紀（1800年代）の作家リストと、20世紀（1900年代）の作家リストを作る
# リスト [ ] なので、後から作家を追加したり削除したりできる
eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgeald", "Orwell"]

# 2つのリストを丸ごと「タプル ( )」に詰め込んで合体させる
# 外側がタプルなので、この「19世紀の箱」と「20世紀の箱」という枠組み自体は、後から変更できない
authors = (eights, nines)

# 完成したタプルを表示する
print(authors)
