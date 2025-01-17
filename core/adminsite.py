from fastapi import FastAPI
from fastapi_amis_admin.amis.components import App
from fastapi_amis_admin.amis_admin.settings import Settings
from fastapi_amis_admin.amis_admin.site import AdminSite, ReDocsAdmin, DocsAdmin
from sqlalchemy.ext.asyncio import AsyncEngine

# 创建后台管理系统
from starlette.requests import Request

site = AdminSite(settings=Settings(debug=True, database_url_async='sqlite+aiosqlite:///admisadmin.db'))


# 自定义后台管理站点
class NewAdminSite(AdminSite):
    # 自定义应用模板,复制原模板文件修改,原路径: fastapi_amis_admin/amis/templates/app.html
    template_name = '/templates/new_app.html'

    def __init__(self, settings: Settings, fastapi: FastAPI = None, engine: AsyncEngine = None):
        super().__init__(settings, fastapi, engine)
        # 取消注册默认管理类
        self.unregister_admin(DocsAdmin, ReDocsAdmin)

    async def get_page(self, request: Request) -> App:
        app = await super().get_page(request)
        # 自定义站点名称,logo信息, 参考: https://baidu.gitee.io/amis/zh-CN/components/app
        app.brandName = 'MyAdminSite'
        app.logo = 'https://baidu.gitee.io/amis/static/logo_408c434.png'
        return app

# site = NewAdminSite(settings=Settings(debug=True, database_url_async='sqlite+aiosqlite:///admisadmin.db'))
