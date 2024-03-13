from enum import Enum


class MESSAGES(str, Enum):
    DEFAULT = lambda msg="": f"{msg if msg else ''}"


class ERROR_MESSAGES(str, Enum):
    def __str__(self) -> str:
        return super().__str__()

    DEFAULT = lambda err="": f"发生错误 :/\n{err if err else ''}"
    ENV_VAR_NOT_FOUND = "找不到所需的环境变量。现在终止。"
    CREATE_USER_ERROR = "哎呀！创建帐户时出现问题。请稍后再试。如果问题仍然存在，请与支持人员联系以获得帮助。"
    DELETE_USER_ERROR = "哎呀！出了问题。尝试删除用户时遇到问题。请再打一次。"
    EMAIL_TAKEN = "哦！此邮箱账号已注册。使用现有帐户登录或选择其他邮箱账号重新开始。"
    USERNAME_TAKEN = (
        "哦！此用户名已注册。请选择其他用户名。"
    )
    COMMAND_TAKEN = "哦！此命令已注册。请选择另一个命令字符串。"
    FILE_EXISTS = "哦！此文件已注册。请选择其他文件。"

    NAME_TAG_TAKEN = "哦！此名称标记已注册。请选择其他名称标记字符串。"
    INVALID_TOKEN = (
        "您的会话已过期或令牌无效。请重新登录。"
    )
    INVALID_CRED = "提供的电子邮件或密码不正确。请检查拼写错误，然后再次尝试登录。"
    INVALID_EMAIL_FORMAT = "您输入的电子邮件格式无效。请仔细检查并确保您使用的是有效的电子邮件地址（例如。，yourname@example.com)."
    INVALID_PASSWORD = (
        "提供的密码不正确。请检查拼写错误，然后重试。"
    )
    UNAUTHORIZED = "401未经授权"
    ACCESS_PROHIBITED = "您没有访问此资源的权限。请与管理员联系以获取帮助。"
    ACTION_PROHIBITED = (
        "请求的操作已作为安全措施受到限制。"
    )

    FILE_NOT_SENT = "FILE_NOT_SENT"
    FILE_NOT_SUPPORTED = "哎呀！似乎不支持您尝试上载的文件格式。请上传一个支持格式的文件（如JPG、PNG、PDF、TXT），然后重试。"

    NOT_FOUND = "我们找不到您要找的内容 :/"
    USER_NOT_FOUND = "我们找不到您要找的内容 :/"
    API_KEY_NOT_FOUND = "哎呀！看起来好像打嗝了。缺少API密钥。请确保提供有效的API密钥以访问此功能。"

    MALICIOUS = "检测到异常活动，请几分钟后重试。"

    PANDOC_NOT_INSTALLED = "服务器上未安装Pandoc。请与管理员联系以获取帮助。"
    INCORRECT_FORMAT = (
        lambda err="": f"无效的格式。请使用正确的格式{err if err else ''}"
    )
    RATE_LIMIT_EXCEEDED = "超过API费率限制"

    MODEL_NOT_FOUND = lambda name="": f"模型 '{name}' 没找到"
    OPENAI_NOT_FOUND = lambda name="": f"OpenAI API 没找到"
