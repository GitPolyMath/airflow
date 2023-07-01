def get_sftp():
    print("sftp 함수를 실행하겠습니다.")

def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타 선택사항: {args}')

def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타 선택사항: {args}')
    email = kwargs.get('email') or ''
    phone = kwargs.get('phone') or ''
    if email:
        print(f'(선택옵션)email: {email}')
    if phone:
        print(f'(선택옵션)phone: {phone}')