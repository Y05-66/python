import requests
import time
import json
import re
import hashlib
from datetime import datetime
import random
from typing import Dict, List, Optional
from bs4 import BeautifulSoup


class QingguoCourseSelector:
    """
    青果教务系统选课类
    适用于: http://jw.hnsoftedu.com/jsxsd/
    """

    def __init__(self, username: str, password: str):
        """
        初始化选课系统

        Args:
            username: 学号
            password: 密码
        """
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.session.headers.update(self.headers)

        # 青果系统的URL
        self.base_url = "http://jw.hnsoftedu.com"
        self.login_page_url = f"{self.base_url}/jsxsd/"
        self.login_url = f"{self.base_url}/jsxsd/xk/LoginToXk"
        self.main_page_url = f"{self.base_url}/jsxsd/framework/xsMain.jsp"

        # 选课相关URL
        self.course_select_main = f"{self.base_url}/jsxsd/xsxk/xsxk_index"  # 选课主页
        self.course_list_url = f"{self.base_url}/jsxsd/xsxkkc/xsxkKcxz"  # 课程列表
        self.select_course_url = f"{self.base_url}/jsxsd/xsxkkc/kcxzSubmit"  # 提交选课

        self.is_logged_in = False

    def encode_password(self, password: str) -> str:
        """
        青果系统密码加密
        通常是MD5加密，但可能需要查看具体的js文件
        """
        # 基础MD5加密
        return hashlib.md5(password.encode()).hexdigest()

    def get_encoded(self, username: str, password: str) -> str:
        """
        获取encoded参数（青果系统特有）
        这个参数是用户名和密码的组合编码
        """
        # 青果系统的encoded算法（可能需要根据实际js调整）
        account = username
        passwd = password
        encoded = account + "%%%" + passwd

        # 转换为Base64或其他编码（根据实际系统）
        import base64
        return base64.b64encode(encoded.encode()).decode()

    def login(self) -> bool:
        """
        登录青果教务系统

        Returns:
            bool: 登录是否成功
        """
        try:
            print(f"[{self.get_timestamp()}] 正在访问登录页面...")

            # 先访问主页，获取session
            self.session.get(self.login_page_url, timeout=10)

            # 构造登录数据
            login_data = {
                'USERNAME': self.username,
                'PASSWORD': self.password,
                # 'encoded': self.get_encoded(self.username, self.password),
            }

            # 如果需要验证码，这里添加验证码处理
            # login_data['RANDOMCODE'] = self.handle_captcha()

            # 发送登录请求
            print(f"[{self.get_timestamp()}] 正在登录...")
            response = self.session.post(
                self.login_url,
                data=login_data,
                headers={
                    **self.headers,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Referer': self.login_page_url
                },
                timeout=10,
                allow_redirects=False
            )

            # 检查是否登录成功
            if response.status_code == 302 or response.status_code == 200:
                # 青果系统登录成功通常会重定向
                # 尝试访问主页验证登录
                main_response = self.session.get(self.main_page_url, timeout=10)

                if '学生个人中心' in main_response.text or '我的桌面' in main_response.text:
                    self.is_logged_in = True

                    # 提取学生姓名（可选）
                    soup = BeautifulSoup(main_response.text, 'html.parser')
                    name_elem = soup.find('div', {'class': 'Nsb_top_menu_nc'})
                    if name_elem:
                        student_name = name_elem.text.strip()
                        print(f"[{self.get_timestamp()}] ✅ 登录成功！欢迎 {student_name}")
                    else:
                        print(f"[{self.get_timestamp()}] ✅ 登录成功！")

                    return True
                else:
                    print(f"[{self.get_timestamp()}] ❌ 登录失败：用户名或密码错误")
                    return False
            else:
                print(f"[{self.get_timestamp()}] ❌ 登录失败：服务器响应异常")
                return False

        except Exception as e:
            print(f"[{self.get_timestamp()}] ❌ 登录出错：{str(e)}")
            return False

    def handle_captcha(self) -> str:
        """
        处理验证码
        """
        # 下载验证码
        captcha_url = f"{self.base_url}/jsxsd/verifycode.servlet"
        response = self.session.get(captcha_url, stream=True)

        # 保存验证码图片
        with open('captcha.jpg', 'wb') as f:
            f.write(response.content)

        print("验证码已保存为 captcha.jpg")
        return input("请输入验证码: ")

    def get_course_list(self, course_type: str = "01") -> List[Dict]:
        """
        获取可选课程列表

        Args:
            course_type: 课程类型
                01: 主修课程
                02: 选修课程
                03: 体育课程
                04: 通识课程

        Returns:
            List[Dict]: 课程列表
        """
        if not self.is_logged_in:
            print("请先登录")
            return []

        try:
            # 先进入选课主页
            self.session.get(f"{self.course_select_main}?kcxx=&skls=&skxq=&skjc=&sfym=&sfct=")

            # 获取课程列表
            params = {
                'kcxx': '',  # 课程信息
                'skls': '',  # 上课老师
                'skxq': '',  # 上课星期
                'skjc': '',  # 上课节次
                'kcxz': course_type,  # 课程性质
                'sfym': '0',  # 是否已满
                'sfct': '0'  # 是否冲突
            }

            response = self.session.get(self.course_list_url, params=params, timeout=10)

            if response.status_code == 200:
                # 解析课程列表
                courses = self.parse_course_list(response.text)
                print(f"[{self.get_timestamp()}] 获取到 {len(courses)} 门可选课程")
                return courses

            return []

        except Exception as e:
            print(f"[{self.get_timestamp()}] 获取课程列表失败：{str(e)}")
            return []

    def parse_course_list(self, html: str) -> List[Dict]:
        """
        解析课程列表HTML
        """
        courses = []
        soup = BeautifulSoup(html, 'html.parser')

        # 查找课程表格
        table = soup.find('table', {'id': 'kctable'})
        if not table:
            return courses

        # 解析每一行课程
        rows = table.find_all('tr')[1:]  # 跳过表头
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 8:
                course = {
                    'id': cols[1].text.strip(),  # 课程号
                    'name': cols[2].text.strip(),  # 课程名
                    'teacher': cols[4].text.strip(),  # 教师
                    'time': cols[5].text.strip(),  # 上课时间
                    'location': cols[6].text.strip(),  # 上课地点
                    'capacity': cols[7].text.strip(),  # 容量
                    'selected': cols[8].text.strip() if len(cols) > 8 else '',  # 已选人数
                }

                # 提取选课按钮的参数
                select_btn = row.find('input', {'type': 'button', 'value': '选课'})
                if select_btn and select_btn.get('onclick'):
                    # 从onclick中提取参数
                    onclick = select_btn['onclick']
                    # 示例: javascript:xkOper('xxx','xxx')
                    match = re.search(r"xkOperKATEX_INLINE_OPEN'([^']+)','([^']+)'KATEX_INLINE_CLOSE", onclick)
                    if match:
                        course['select_params'] = {
                            'param1': match.group(1),
                            'param2': match.group(2)
                        }

                courses.append(course)

        return courses

    def select_course(self, course_id: str, course_name: str = "", select_params: Dict = None) -> bool:
        """
        选课

        Args:
            course_id: 课程ID
            course_name: 课程名称
            select_params: 选课参数（从课程列表中获取）

        Returns:
            bool: 选课是否成功
        """
        if not self.is_logged_in:
            print("请先登录")
            return False

        try:
            # 构造选课请求数据
            select_data = {
                'kcid': course_id,  # 课程ID
                'kcmc': course_name,  # 课程名称
            }

            # 如果有额外参数
            if select_params:
                select_data.update(select_params)

            # 发送选课请求
            response = self.session.post(
                self.select_course_url,
                data=select_data,
                headers={
                    **self.headers,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Referer': self.course_list_url
                },
                timeout=10
            )

            if response.status_code == 200:
                result_text = response.text

                # 解析返回结果
                if '选课成功' in result_text:
                    print(f"[{self.get_timestamp()}] ✅ 成功选中课程：{course_name or course_id}")
                    return True
                elif '课程时间冲突' in result_text:
                    print(f"[{self.get_timestamp()}] ❌ 课程时间冲突：{course_name or course_id}")
                elif '已满' in result_text or '人数已达上限' in result_text:
                    print(f"[{self.get_timestamp()}] ⚠️ 课程已满：{course_name or course_id}")
                elif '已选' in result_text:
                    print(f"[{self.get_timestamp()}] ℹ️ 已经选过该课程：{course_name or course_id}")
                    return True
                else:
                    print(f"[{self.get_timestamp()}] ❌ 选课失败：{course_name or course_id}")
                    print(f"    返回信息：{result_text[:100]}")

            return False

        except Exception as e:
            print(f"[{self.get_timestamp()}] 选课请求出错：{str(e)}")
            return False

    def auto_select_courses(self, target_courses: List[Dict],
                            max_attempts: int = 50,
                            interval: float = 2.0):
        """
        自动抢课

        Args:
            target_courses: 目标课程列表
            max_attempts: 最大尝试次数
            interval: 请求间隔（秒）
        """
        if not self.is_logged_in:
            if not self.login():
                print("登录失败，无法抢课")
                return

        print(f"[{self.get_timestamp()}] 开始抢课")
        print(f"目标课程：{len(target_courses)} 门")
        print(f"最大尝试：{max_attempts} 次")
        print(f"请求间隔：{interval} 秒")
        print("-" * 50)

        selected_courses = []
        remaining_courses = target_courses.copy()

        for attempt in range(1, max_attempts + 1):
            print(f"\n[{self.get_timestamp()}] 第 {attempt}/{max_attempts} 次尝试")

            for course in remaining_courses[:]:
                success = self.select_course(
                    course['id'],
                    course.get('name', ''),
                    course.get('select_params')
                )

                if success:
                    selected_courses.append(course)
                    remaining_courses.remove(course)
                    print(f"[{self.get_timestamp()}] 进度：{len(selected_courses)}/{len(target_courses)}")

                # 随机延迟，避免请求过快
                time.sleep(random.uniform(0.5, 1.5))

            if not remaining_courses:
                print(f"\n[{self.get_timestamp()}] 🎉 所有课程选课成功！")
                break

            if attempt < max_attempts:
                print(f"[{self.get_timestamp()}] 等待 {interval} 秒...")
                time.sleep(interval)

        # 输出统计
        print("\n" + "=" * 50)
        print(f"[{self.get_timestamp()}] 抢课结束")
        print(f"成功：{len(selected_courses)}/{len(target_courses)} 门")

        if selected_courses:
            print("\n✅ 成功选中的课程：")
            for course in selected_courses:
                print(f"  - {course.get('name', course['id'])}")

        if remaining_courses:
            print("\n❌ 未成功的课程：")
            for course in remaining_courses:
                print(f"  - {course.get('name', course['id'])}")

    @staticmethod
    def get_timestamp() -> str:
        """获取当前时间戳"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 使用示例
def main():
    """主函数"""

    print("=" * 50)
    print("青果教务系统选课助手")
    print("目标系统：http://jw.hnsoftedu.com/jsxsd/")
    print("=" * 50)

    # 配置你的账号信息
    config = {
        "username": "202401550204",  # ⚠️ 在这里填入你的学号
        "password": "*YjX200501040073",  # ⚠️ 在这里填入你的密码
        "target_courses": [
            # ⚠️ 在这里填入要抢的课程信息
            # 可以先运行 get_course_list() 获取课程ID
            {"id": "01001208", "name": "大学美育"},
            {"id": "01002030", "name": "中国古典诗词赏析"},
        ],
        "max_attempts": 30,  # 最大尝试次数
        "interval": 2.0  # 请求间隔（秒）
    }

    # 创建选课器
    selector = QingguoCourseSelector(config["username"], config["password"])

    # 登录系统
    if selector.login():
        # 可选：先获取并显示可选课程列表
        print("\n正在获取可选课程列表...")
        courses = selector.get_course_list("01")  # 01表示主修课程
        if courses:
            print("\n可选课程列表：")
            for i, course in enumerate(courses[:10], 1):  # 只显示前10个
                print(f"{i}. [{course['id']}] {course['name']} - {course['teacher']} - {course['time']}")

        # 开始自动选课
        input("\n按Enter键开始抢课...")
        selector.auto_select_courses(
            target_courses=config["target_courses"],
            max_attempts=config["max_attempts"],
            interval=config["interval"]
        )
    else:
        print("登录失败，请检查账号密码")


# 辅助功能：探索系统结构
def explore_system():
    """
    探索教务系统结构，帮助理解系统
    """
    username = input("请输入学号: ")
    password = input("请输入密码: ")

    selector = QingguoCourseSelector(username, password)

    if selector.login():
        print("\n登录成功！正在分析系统...")

        # 获取各类课程
        course_types = {
            "01": "主修课程",
            "02": "选修课程",
            "03": "体育课程",
            "04": "通识课程"
        }

        for type_code, type_name in course_types.items():
            print(f"\n正在获取{type_name}...")
            courses = selector.get_course_list(type_code)
            if courses:
                print(f"找到 {len(courses)} 门{type_name}")
                # 显示第一门课程的详细信息作为示例
                if courses:
                    print(f"示例课程信息：{json.dumps(courses[0], ensure_ascii=False, indent=2)}")


if __name__ == "__main__":
    # 运行主程序
    main()

    # 或者运行探索程序来了解系统
    # explore_system()