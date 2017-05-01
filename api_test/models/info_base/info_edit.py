from api_test.models.info_base.info_model import Info


def info_add(info_dict):
    new_info = Info()
    new_info.code = info_dict['code']
    new_info.pwd = info_dict['pwd']
    new_info.name = info_dict['name']
    new_info.company_type = info_dict['company_type']
    new_info.address = info_dict['address']
    new_info.comment = info_dict['comment']
    new_info.principal_name = info_dict['principal_name']
    new_info.principal_phone = info_dict['principal_phone']
    new_info.contacts_name = info_dict['contacts_name']
    new_info.contacts_phone = info_dict['contacts_phone']
    new_info.hotline = info_dict['hotline']
    new_info.authentication = info_dict['authentication']
    if info_dict['email'] is not None:
        new_info.email = info_dict['email']
    new_info.logo_base64(info_dict['logo'])
    new_info.licence_base64(info_dict['business_licence'])
    new_info.qualification_base64(info_dict['qualification'])
    new_info.save()