class Node:
    # 단순 연결 리스트를 위한 노드 클래스
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        # 현재 노드 다음에 새 노드 삽입
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        # 현재 노드의 다음 노드를 삭제하고 반환
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


class Book:
    # 도서 정보를 저장하는 클래스
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # 도서 정보를 보기 좋게 출력
        return f"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]"


class LinkedList:
    # 단순 연결 리스트
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, book):
        # 도서를 리스트 맨 앞에 삽입
        new_node = Node(book)
        new_node.link = self.head
        self.head = new_node

    def find_by_title(self, title):
        # 책 제목으로 도서를 찾기
        current = self.head
        while current is not None:
            if current.data.title == title:
                return current.data
            current = current.link
        return None

    def find_pos_by_title(self, title):
        # 책 제목으로 도서의 위치(노드와 이전 노드) 찾기
        prev = None
        current = self.head
        while current is not None:
            if current.data.title == title:
                return prev, current
            prev = current
            current = current.link
        return None, None

    def find_by_id(self, book_id):
        # 책 번호로 도서를 찾기
        current = self.head
        while current is not None:
            if current.data.book_id == book_id:
                return current.data
            current = current.link
        return None

    def delete_by_title(self, title):
        # 책 제목으로 도서 삭제
        prev, current = self.find_pos_by_title(title)
        if current is None:
            return False
        if prev is None:  # 첫 번째 노드 삭제
            self.head = current.link
        else:
            prev.popNext()
        return True

    def print_all(self):
        # 전체 도서 목록 출력
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        current = self.head
        while current is not None:
            print(current.data)
            current = current.link


class BookManagement:
    # 도서 관리 기능을 제공하는 클래스
    def __init__(self):
        self.book_list = LinkedList()

    def add_book(self, book_id, title, author, year):
        # 도서 추가
        if self.book_list.find_by_id(book_id) is not None:
            print("오류: 이미 존재하는 책 번호입니다.")
            return
        new_book = Book(book_id, title, author, year)
        self.book_list.insert(new_book)
        print(f"책 제목 '{new_book.title}' 도서가 추가되었습니다.")

    def remove_book(self, title):
        # 책 제목으로 도서 삭제
        if self.book_list.delete_by_title(title):
            print(f"책 제목 '{title}'의 도서가 삭제되었습니다.")
        else:
            print(f"오류: 책 제목 '{title}' 도서를 찾을 수 없습니다.")

    def search_book(self, title):
        # 책 제목으로 도서 조회
        book = self.book_list.find_by_title(title)
        if book is not None:
            print("도서 조회 결과:")
            print(book)
        else:
            print(f"오류: 책 제목 '{title}' 도서를 찾을 수 없습니다.")

    def display_books(self):
        # 전체 도서 목록 출력
        print("\n==== 전체 도서 목록 ====")
        self.book_list.print_all()
        print("=====================\n")

    def run(self):
        # 프로그램 실행
        while True:
            print("\n======== 도서 관리 프로그램 ========")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            choice = input("메뉴 선택: ")

            if choice == '1':
                try:
                    book_id = int(input("책 번호를 입력하십시오: "))
                    title = input("책 제목을 입력하십시오: ")
                    author = input("저자를 입력하십시오: ")
                    year = input("출판 연도를 입력하십시오: ")
                    self.add_book(book_id, title, author, year)
                except ValueError:
                    print("오류: 책 번호는 숫자로 입력해야 합니다.")

            elif choice == '2':
                title = input("삭제할 책 제목을 입력하십시오: ")
                self.remove_book(title)

            elif choice == '3':
                title = input("조회할 책 제목을 입력하십시오: ")
                self.search_book(title)

            elif choice == '4':
                self.display_books()

            elif choice == '5':
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 1 ~ 5 사이의 번호를 입력하세요.")

if __name__ == "__main__":
    manager = BookManagement()
    manager.run()
