# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

from tb_rest_client.rest_client_base import *
from tb_rest_client.api.api_pe import *


logger = getLogger(__name__)


class RestClientPE(RestClientBase):
    def __init__(self, base_url):
        super().__init__(base_url)

    def login(self, username, password):
        super(RestClientPE, self).login(username=username, password=password)
        self.__load_controllers()

    def public_login(self, public_id):
        super(RestClientPE, self).public_login(public_id=public_id)
        self.__load_controllers()

    def token_login(self, token, refresh_token=None):
        super(RestClientPE, self).token_login(token=token, refresh_token=refresh_token)
        self.__load_controllers()

    # Self Registration Controller
    def get_privacy_policy(self, ):
        return self.self_registration_controller.get_privacy_policy_using_get()

    def get_self_registration_params(self, ):
        return self.self_registration_controller.get_self_registration_params_using_get()

    def get_sign_up_self_registration_params(self, pkg_name=None):
        return self.self_registration_controller.get_sign_up_self_registration_params_using_get(pkg_name=pkg_name)

    def get_terms_of_use(self, ):
        return self.self_registration_controller.get_terms_of_use_using_get()

    def save_self_registration_params(self, body=None):
        return self.self_registration_controller.save_self_registration_params_using_post(body=body)

    # O Auth 2 Config Template Controller
    def delete_client_registration_template(self, client_registration_template_id: EntityId):
        client_registration_template_id = self.get_id(client_registration_template_id)
        return self.o_auth2_config_template_controller.delete_client_registration_template_using_delete(
            client_registration_template_id=client_registration_template_id)

    def get_client_registration_templates(self, ):
        return self.o_auth2_config_template_controller.get_client_registration_templates_using_get()

    def save_client_registration_template(self, body=None):
        return self.o_auth2_config_template_controller.save_client_registration_template_using_post(body=body)

    # HTTP Integration Controller
    def http_check_status_get(self, routing_key: str, request_params: dict, request_headers: dict):
        return self.http_integration_controller.check_status_using_get(routing_key=routing_key,
                                                                       request_params=request_params,
                                                                       request_headers=request_headers)

    def http_process_request_v1_post1(self, routing_key: str, suffix: str):
        return self.http_integration_controller.process_request_using_post1(routing_key=routing_key, suffix=suffix)

    def http_process_request_v2_post2(self, routing_key: str, suffix: str):
        return self.http_integration_controller.process_request_using_post2(routing_key=routing_key, suffix=suffix)

    def get_asset_types(self, ):
        return self.asset_controller.get_asset_types_using_get()

    def find_by_query(self, body=None):
        return self.asset_controller.find_by_query_using_post(body=body)

    def get_tenant_assets(self, page_size: str, page: str, type=None, text_search=None, sort_property=None,
                          sort_order=None):
        return self.asset_controller.get_tenant_assets_using_get(page_size=int(page_size), page=int(page), type=type,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    # Asset Controller
    def delete_asset(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.delete_asset_using_delete(asset_id=asset_id)

    def asset_find_by_query(self, body=None):
        return self.asset_controller.find_by_query_using_post(body=body)

    def get_customer_assets(self, customer_id: CustomerId, page_size: int, page: int, type=None, text_search=None,
                            sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.asset_controller.get_customer_assets_using_get(customer_id=customer_id, page_size=page_size,
                                                                   page=page, type=type, text_search=text_search,
                                                                   sort_property=sort_property, sort_order=sort_order)

    def process_asset_bulk_import(self, body=None):
        return self.asset_controller.process_asset_bulk_import_using_post(body=body)

    def get_tenant_asset(self, asset_name: str):
        return self.asset_controller.get_tenant_asset_using_get(asset_name=asset_name)

    def get_asset_by_id(self, asset_id: AssetId):
        asset_id = self.get_id(asset_id)
        return self.asset_controller.get_asset_by_id_using_get(asset_id=asset_id)

    def get_assets_by_ids(self, asset_ids: list):
        return self.asset_controller.get_assets_by_ids_using_get(asset_ids=str(asset_ids))

    def save_asset(self, body=None, entity_group_id=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.asset_controller.save_asset_using_post(body=body, entity_group_id=entity_group_id)

    def asset_get_tenant_assets(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                                sort_order=None):
        return self.asset_controller.get_tenant_assets_using_get(page_size=page_size, page=page, type=type,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def asset_get_asset_types(self, ):
        return self.asset_controller.get_asset_types_using_get()

    def delete_device_group_ota_package(self, id: str):
        return self.device_group_ota_package_controller.delete_device_group_ota_package_using_delete(id=id)

    def get_firmware_by_id(self, group_id: EntityGroupId, firmware_type: str):
        group_id = self.get_id(group_id)
        return self.device_group_ota_package_controller.get_firmware_by_id_using_get(group_id=group_id,
                                                                                     firmware_type=firmware_type)

    def save_device_group_ota_package(self, body=None):
        return self.device_group_ota_package_controller.save_device_group_ota_package_using_post(body=body)

    def find_by_query_v2(self, body=None):
        return self.edge_controller.find_by_query_using_post2(body=body)

    def sync_edge(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.sync_edge_using_post(edge_id=edge_id)

    def check_instance(self, body=None):
        return self.edge_controller.check_instance_using_post(body=body)

    def get_tenant_edges(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                         sort_order=None):
        return self.edge_controller.get_tenant_edges_using_get(page_size=page_size, page=page, type=type,
                                                               text_search=text_search, sort_property=sort_property,
                                                               sort_order=sort_order)

    def find_missing_to_related_rule_chains(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.find_missing_to_related_rule_chains_using_get(edge_id=edge_id)

    def get_customer_edges(self, customer_id: CustomerId, page_size: int, page: int, type=None, text_search=None,
                           sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.edge_controller.get_customer_edges_using_get(customer_id=customer_id, page_size=page_size,
                                                                 page=page, type=type, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order)

    def process_edges_bulk_import(self, body=None):
        return self.edge_controller.process_edges_bulk_import_using_post(body=body)

    def activate_instance(self, license_secret: str, release_date: str):
        return self.edge_controller.activate_instance_using_post(license_secret=license_secret,
                                                                 release_date=release_date)

    def get_tenant_edge(self, edge_name: str):
        return self.edge_controller.get_tenant_edge_using_get(edge_name=edge_name)

    def get_edge_by_id(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.get_edge_by_id_using_get(edge_id=edge_id)

    def delete_edge(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.edge_controller.delete_edge_using_delete(edge_id=edge_id)

    def save_edge(self, body=None, entity_group_id=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.edge_controller.save_edge_using_post(body=body, entity_group_id=entity_group_id)

    def is_edges_support_enabled(self, ):
        return self.edge_controller.is_edges_support_enabled_using_get()

    def get_edges(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.edge_controller.get_edges_using_get(page_size=page_size, page=page, text_search=text_search,
                                                        sort_property=sort_property, sort_order=sort_order)

    def get_edge_types(self, ):
        return self.edge_controller.get_edge_types_using_get()

    def set_edge_root_rule_chain(self, edge_id: EdgeId, rule_chain_id: RuleChainId):
        edge_id = self.get_id(edge_id)
        rule_chain_id = self.get_id(rule_chain_id)
        return self.edge_controller.set_edge_root_rule_chain_using_post(edge_id=edge_id, rule_chain_id=rule_chain_id)

    def get_edges_by_ids(self, edge_ids: list):
        return self.edge_controller.get_edges_by_ids_using_get(edge_ids=str(edge_ids))

    def ocean_connect_process_request_v2_delete2(self, body: str, request_headers: dict, routing_key: str):
        return self.ocean_connect_integration_controller.process_request_using_delete2(body=body,
                                                                                       request_headers=request_headers,
                                                                                       routing_key=routing_key)

    def ocean_connect_process_request_v2_get2(self, body: str, request_headers: dict, routing_key: str):
        return self.ocean_connect_integration_controller.process_request_using_get2(body=body,
                                                                                    request_headers=request_headers,
                                                                                    routing_key=routing_key)

    def ocean_connect_process_request_v2_head2(self, body: str, request_headers: dict, routing_key: str):
        return self.ocean_connect_integration_controller.process_request_using_head2(body=body,
                                                                                     request_headers=request_headers,
                                                                                     routing_key=routing_key)

    def ocean_connect_process_request_v2_options2(self, body: str, request_headers: dict, routing_key: str):
        return self.ocean_connect_integration_controller.process_request_using_options2(body=body,
                                                                                        request_headers=request_headers,
                                                                                        routing_key=routing_key)

    def ocean_connect_process_request_v2_patch2(self, body: str, request_headers: dict, routing_key: str):
        return self.ocean_connect_integration_controller.process_request_using_patch2(body=body,
                                                                                      request_headers=request_headers,
                                                                                      routing_key=routing_key)

    def ocean_connect_process_request_v10_post10(self, body: str, request_headers: dict, routing_key: str):
        return self.ocean_connect_integration_controller.process_request_using_post10(body=body,
                                                                                      request_headers=request_headers,
                                                                                      routing_key=routing_key)

    def ocean_connect_process_request_v2_put2(self, body: str, request_headers: dict, routing_key: str):
        return self.ocean_connect_integration_controller.process_request_using_put2(body=body,
                                                                                    request_headers=request_headers,
                                                                                    routing_key=routing_key)

    def get_allowed_permissions(self, ):
        return self.user_permissions_controller.get_allowed_permissions_using_get()

    def change_owner_to_customer(self, owner_id: UserId, entity_type: str, entity_id: EntityId):
        owner_id = self.get_id(owner_id)
        entity_id = self.get_id(entity_id)
        return self.owner_controller.change_owner_to_customer_using_post(owner_id=owner_id, entity_type=entity_type,
                                                                         entity_id=entity_id)

    def change_owner_to_tenant(self, owner_id: UserId, entity_type: str, entity_id: EntityId):
        owner_id = self.get_id(owner_id)
        entity_id = self.get_id(entity_id)
        return self.owner_controller.change_owner_to_tenant_using_post(owner_id=owner_id, entity_type=entity_type,
                                                                       entity_id=entity_id)

    def get_persisted_rpc(self, rpc_id: RpcId):
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def rpc_v2_get_persisted_rpc(self, rpc_id: RpcId):
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.get_persisted_rpc_using_get(rpc_id=rpc_id)

    def handle_one_way_device_rpc_request_v1(self, device_id: DeviceId, body=None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_one_way_device_rpc_request_using_post1(device_id=device_id, body=body)

    def handle_two_way_device_rpc_request_v1(self, device_id: DeviceId, body=None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.handle_two_way_device_rpc_request_using_post1(device_id=device_id, body=body)

    def get_persisted_rpc_by_device(self, device_id: DeviceId, page_size: int, page: int, rpc_status: str,
                                    text_search=None, sort_property=None, sort_order=None):
        device_id = self.get_id(device_id)
        return self.rpc_v2_controller.get_persisted_rpc_by_device_using_get(device_id=device_id, page_size=page_size,
                                                                            page=page, rpc_status=rpc_status,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def delete_resource(self, rpc_id: RpcId):
        rpc_id = self.get_id(rpc_id)
        return self.rpc_v2_controller.delete_resource_using_delete(rpc_id=rpc_id)

    def get_edge_events(self, edge_id: EdgeId, page_size: int, page: int, text_search=None, sort_property=None,
                        sort_order=None, start_time=None, end_time=None):
        edge_id = self.get_id(edge_id)
        return self.edge_event_controller.get_edge_events_using_get(edge_id=edge_id, page_size=page_size, page=page,
                                                                    text_search=text_search,
                                                                    sort_property=sort_property, sort_order=sort_order,
                                                                    start_time=start_time, end_time=end_time)

    def get_customer_title_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_title_by_id_using_get(customer_id=customer_id)

    def get_customers(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.customer_controller.get_customers_using_get(page_size=page_size, page=page, text_search=text_search,
                                                                sort_property=sort_property, sort_order=sort_order)

    def get_customer_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_customer_by_id_using_get(customer_id=customer_id)

    def get_short_customer_info_by_id(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.get_short_customer_info_by_id_using_get(customer_id=customer_id)

    def save_customer(self, body=None, entity_group_id=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.customer_controller.save_customer_using_post(body=body, entity_group_id=entity_group_id)

    def get_tenant_customer(self, customer_title: str):
        return self.customer_controller.get_tenant_customer_using_get(customer_title=customer_title)

    def delete_customer(self, customer_id: CustomerId):
        customer_id = self.get_id(customer_id)
        return self.customer_controller.delete_customer_using_delete(customer_id=customer_id)

    def get_user_token(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_token_using_get(user_id=user_id)

    def get_activation_link(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_activation_link_using_get(user_id=user_id)

    def get_user_users(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.user_controller.get_user_users_using_get(page_size=page_size, page=page, text_search=text_search,
                                                             sort_property=sort_property, sort_order=sort_order)

    def delete_user(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.delete_user_using_delete(user_id=user_id)

    def get_all_customer_users(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.user_controller.get_all_customer_users_using_get(page_size=page_size, page=page,
                                                                     text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order)

    def set_user_credentials_enabled(self, user_id: UserId, user_credentials_enabled=None):
        user_id = self.get_id(user_id)
        return self.user_controller.set_user_credentials_enabled_using_post(user_id=user_id,
                                                                            user_credentials_enabled=user_credentials_enabled)

    def get_customer_users(self, customer_id: CustomerId, page_size: int, page: int, text_search=None,
                           sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.user_controller.get_customer_users_using_get(customer_id=customer_id, page_size=page_size,
                                                                 page=page, text_search=text_search,
                                                                 sort_property=sort_property, sort_order=sort_order)

    def get_user_by_id(self, user_id: UserId):
        user_id = self.get_id(user_id)
        return self.user_controller.get_user_by_id_using_get(user_id=user_id)

    def get_tenant_admins(self, tenant_id: TenantId, page_size: int, page: int, text_search=None, sort_property=None,
                          sort_order=None):
        tenant_id = self.get_id(tenant_id)
        return self.user_controller.get_tenant_admins_using_get(tenant_id=tenant_id, page_size=page_size, page=page,
                                                                text_search=text_search, sort_property=sort_property,
                                                                sort_order=sort_order)

    def is_user_token_access_enabled(self, ):
        return self.user_controller.is_user_token_access_enabled_using_get()

    def get_users_by_ids(self, user_ids: list):
        return self.user_controller.get_users_by_ids_using_get(user_ids=str(user_ids))

    def save_user(self, body=None, send_activation_mail=None, entity_group_id=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.user_controller.save_user_using_post(body=body, send_activation_mail=send_activation_mail,
                                                         entity_group_id=entity_group_id)

    def send_activation_email(self, email: str):
        return self.user_controller.send_activation_email_using_post(email=email)

    def get_users_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int, text_search=None,
                                     sort_property=None, sort_order=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.user_controller.get_users_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                           page_size=page_size, page=page,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def delete_group_permission(self, group_permission_id: GroupPermissionId):
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.delete_group_permission_using_delete(
            group_permission_id=group_permission_id)

    def get_entity_group_permissions(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        return self.group_permission_controller.get_entity_group_permissions_using_get(entity_group_id=entity_group_id)

    def get_group_permission_by_id(self, group_permission_id: GroupPermissionId):
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_by_id_using_get(
            group_permission_id=group_permission_id)

    def get_group_permission_info_by_id(self, group_permission_id: GroupPermissionId, is_user_group: bool):
        group_permission_id = self.get_id(group_permission_id)
        return self.group_permission_controller.get_group_permission_info_by_id_using_get(
            group_permission_id=group_permission_id, is_user_group=is_user_group)

    def get_user_group_permissions(self, user_group_id: EntityId):
        user_group_id = self.get_id(user_group_id)
        return self.group_permission_controller.get_user_group_permissions_using_get(user_group_id=user_group_id)

    def load_user_group_permission_infos(self, body=None):
        return self.group_permission_controller.load_user_group_permission_infos_using_post(body=body)

    def save_group_permission(self, body=None):
        return self.group_permission_controller.save_group_permission_using_post(body=body)

    def get_device_types(self, ):
        return self.device_controller.get_device_types_using_get()

    def process_devices_bulk_import(self, body=None):
        return self.device_controller.process_devices_bulk_import_using_post(body=body)

    def count_by_device_profile_and_empty_ota_package(self, ota_package_type: str, device_profile_id: DeviceProfileId):
        device_profile_id = self.get_id(device_profile_id)
        return self.device_controller.count_by_device_profile_and_empty_ota_package_using_get(
            ota_package_type=ota_package_type, device_profile_id=device_profile_id)

    def get_devices_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                       text_search=None, sort_property=None, sort_order=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.device_controller.get_devices_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                               page_size=page_size, page=page,
                                                                               text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    def get_devices_by_ids(self, device_ids: list):
        return self.device_controller.get_devices_by_ids_using_get(device_ids=str(device_ids))

    def get_user_devices(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                         sort_order=None):
        return self.device_controller.get_user_devices_using_get(page_size=page_size, page=page, type=type,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def claim_device(self, device_name: str, body=None, sub_customer_id=None):
        sub_customer_id = self.get_id(sub_customer_id)
        return self.device_controller.claim_device_using_post(device_name=device_name, body=body,
                                                              sub_customer_id=sub_customer_id)

    def save_device_with_credentials(self, body=None, entity_group_id=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.device_controller.save_device_with_credentials_using_post(body=body,
                                                                              entity_group_id=entity_group_id)

    def update_device_credentials(self, body=None):
        return self.device_controller.update_device_credentials_using_post(body=body)

    def save_device(self, body=None, access_token=None, entity_group_id=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.device_controller.save_device_using_post(body=body, access_token=access_token,
                                                             entity_group_id=entity_group_id)

    def get_device_by_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_by_id_using_get(device_id=device_id)

    def get_tenant_devices(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                           sort_order=None):
        return self.device_controller.get_tenant_devices_using_get(page_size=page_size, page=page, type=type,
                                                                   text_search=text_search, sort_property=sort_property,
                                                                   sort_order=sort_order)

    def get_customer_devices(self, customer_id: CustomerId, page_size: int, page: int, type=None, text_search=None,
                             sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.device_controller.get_customer_devices_using_get(customer_id=customer_id, page_size=page_size,
                                                                     page=page, type=type, text_search=text_search,
                                                                     sort_property=sort_property, sort_order=sort_order)

    def assign_device_to_tenant(self, tenant_id: TenantId, device_id: DeviceId):
        tenant_id = self.get_id(tenant_id)
        device_id = self.get_id(device_id)
        return self.device_controller.assign_device_to_tenant_using_post(tenant_id=tenant_id, device_id=device_id)

    def find_by_query_v1(self, body=None):
        return self.device_controller.find_by_query_using_post1(body=body)

    def count_by_device_group_and_empty_ota_package(self, ota_package_type: str, ota_package_id: OtaPackageId,
                                                    entity_group_id: EntityGroupId):
        ota_package_id = self.get_id(ota_package_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.device_controller.count_by_device_group_and_empty_ota_package_using_get(
            ota_package_type=ota_package_type, ota_package_id=ota_package_id, entity_group_id=entity_group_id)

    def delete_device(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.delete_device_using_delete(device_id=device_id)

    def re_claim_device(self, device_name: str):
        return self.device_controller.re_claim_device_using_delete(device_name=device_name)

    def get_tenant_device(self, device_name: str):
        return self.device_controller.get_tenant_device_using_get(device_name=device_name)

    def get_device_credentials_by_device_id(self, device_id: DeviceId):
        device_id = self.get_id(device_id)
        return self.device_controller.get_device_credentials_by_device_id_using_get(device_id=device_id)

    def delete_converter(self, converter_id: ConverterId):
        converter_id = self.get_id(converter_id)
        return self.converter_controller.delete_converter_using_delete(converter_id=converter_id)

    def get_converter_by_id(self, converter_id: ConverterId):
        converter_id = self.get_id(converter_id)
        return self.converter_controller.get_converter_by_id_using_get(converter_id=converter_id)

    def get_converters_by_ids(self, converter_ids: list):
        return self.converter_controller.get_converters_by_ids_using_get(converter_ids=str(converter_ids))

    def get_converters(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.converter_controller.get_converters_using_get(page_size=page_size, page=page,
                                                                  text_search=text_search, sort_property=sort_property,
                                                                  sort_order=sort_order)

    def get_latest_converter_debug_input(self, converter_id: ConverterId):
        converter_id = self.get_id(converter_id)
        return self.converter_controller.get_latest_converter_debug_input_using_get(converter_id=converter_id)

    def save_converter(self, body=None):
        return self.converter_controller.save_converter_using_post(body=body)

    def test_down_link_converter(self, body=None):
        return self.converter_controller.test_down_link_converter_using_post(body=body)

    def test_up_link_converter(self, body=None):
        return self.converter_controller.test_up_link_converter_using_post(body=body)

    def get_entity_view_types(self, ):
        return self.entity_view_controller.get_entity_view_types_using_get()

    def delete_entity_view(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.delete_entity_view_using_delete(entity_view_id=entity_view_id)

    def get_entity_view_by_id(self, entity_view_id: EntityViewId):
        entity_view_id = self.get_id(entity_view_id)
        return self.entity_view_controller.get_entity_view_by_id_using_get(entity_view_id=entity_view_id)

    def get_tenant_entity_view(self, entity_view_name: str):
        return self.entity_view_controller.get_tenant_entity_view_using_get(entity_view_name=entity_view_name)

    def get_user_entity_views(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                              sort_order=None):
        return self.entity_view_controller.get_user_entity_views_using_get(page_size=page_size, page=page, type=type,
                                                                           text_search=text_search,
                                                                           sort_property=sort_property,
                                                                           sort_order=sort_order)

    def get_entity_views_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                            text_search=None, sort_property=None, sort_order=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_view_controller.get_entity_views_by_entity_group_id_using_get(
            entity_group_id=entity_group_id, page_size=page_size, page=page, text_search=text_search,
            sort_property=sort_property, sort_order=sort_order)

    def get_entity_views_by_ids(self, entity_view_ids: list):
        return self.entity_view_controller.get_entity_views_by_ids_using_get(entity_view_ids=str(entity_view_ids))

    def save_entity_view(self, body=None, entity_group_id=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_view_controller.save_entity_view_using_post(body=body, entity_group_id=entity_group_id)

    def get_tenant_entity_views(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                                sort_order=None):
        return self.entity_view_controller.get_tenant_entity_views_using_get(page_size=page_size, page=page, type=type,
                                                                             text_search=text_search,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    def find_by_query_v4(self, body=None):
        return self.entity_view_controller.find_by_query_using_post4(body=body)

    def get_customer_entity_views(self, customer_id: CustomerId, page_size: int, page: int, type=None, text_search=None,
                                  sort_property=None, sort_order=None):
        customer_id = self.get_id(customer_id)
        return self.entity_view_controller.get_customer_entity_views_using_get(customer_id=customer_id,
                                                                               page_size=page_size, page=page,
                                                                               type=type, text_search=text_search,
                                                                               sort_property=sort_property,
                                                                               sort_order=sort_order)

    def handle_rule_engine_request(self, entity_type: str, entity_id: EntityId, timeout: int, body=None):
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_using_post(entity_type=entity_type,
                                                                                 entity_id=entity_id, timeout=timeout,
                                                                                 body=body)

    def handle_rule_engine_request_v1(self, entity_type: str, entity_id: EntityId, body=None):
        entity_id = self.get_id(entity_id)
        return self.rule_engine_controller.handle_rule_engine_request_using_post1(entity_type=entity_type,
                                                                                  entity_id=entity_id, body=body)

    def handle_rule_engine_request_v2(self, body=None):
        return self.rule_engine_controller.handle_rule_engine_request_using_post2(body=body)

    def get_admin_settings(self, key: str, system_by_default=None):
        return self.admin_controller.get_admin_settings_using_get(key=key, system_by_default=system_by_default)

    def check_updates(self, ):
        return self.admin_controller.check_updates_using_get()

    def send_test_sms(self, body=None):
        return self.admin_controller.send_test_sms_using_post(body=body)

    def get_security_settings(self, ):
        return self.admin_controller.get_security_settings_using_get()

    def send_test_mail(self, body=None):
        return self.admin_controller.send_test_mail_using_post(body=body)

    def save_admin_settings(self, body=None):
        return self.admin_controller.save_admin_settings_using_post(body=body)

    def save_security_settings(self, body=None):
        return self.admin_controller.save_security_settings_using_post(body=body)

    def t_mobile_iot_cdp_process_request_v4_delete4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_delete4(body=body,
                                                                                          request_headers=request_headers,
                                                                                          routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_get4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_get4(body=body,
                                                                                       request_headers=request_headers,
                                                                                       routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_head4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_head4(body=body,
                                                                                        request_headers=request_headers,
                                                                                        routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_options4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_options4(body=body,
                                                                                           request_headers=request_headers,
                                                                                           routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_patch4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_patch4(body=body,
                                                                                         request_headers=request_headers,
                                                                                         routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v12_post12(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_post12(body=body,
                                                                                         request_headers=request_headers,
                                                                                         routing_key=routing_key)

    def t_mobile_iot_cdp_process_request_v4_put4(self, body: str, request_headers: dict, routing_key: str):
        return self.t_mobile_iot_cdp_integration_controller.process_request_using_put4(body=body,
                                                                                       request_headers=request_headers,
                                                                                       routing_key=routing_key)

    def get_recaptcha_public_key(self, ):
        return self.sign_up_controller.get_recaptcha_public_key_using_get()

    def sign_up(self, body=None):
        return self.sign_up_controller.sign_up_using_post(body=body)

    def accept_privacy_policy(self, ):
        return self.sign_up_controller.accept_privacy_policy_using_post()

    def resend_cloud_email_activation(self, email: str):
        return self.sign_up_controller.resend_cloud_email_activation_using_post(email=email)

    def set_not_display_welcome(self, ):
        return self.sign_up_controller.set_not_display_welcome_using_post()

    def activate_cloud_email(self, email_code: str):
        return self.sign_up_controller.activate_cloud_email_using_get(email_code=email_code)

    def resend_email_activation(self, email: str, pkg_name=None):
        return self.sign_up_controller.resend_email_activation_using_post(email=email, pkg_name=pkg_name)

    def activate_user_by_email_code(self, email_code: str, pkg_name=None):
        return self.sign_up_controller.activate_user_by_email_code_using_post(email_code=email_code, pkg_name=pkg_name)

    def privacy_policy_accepted(self, ):
        return self.sign_up_controller.privacy_policy_accepted_using_get()

    def accept_terms_of_use(self, ):
        return self.sign_up_controller.accept_terms_of_use_using_post()

    def activate_cloud_user_by_email_code(self, email_code: str):
        return self.sign_up_controller.activate_cloud_user_by_email_code_using_post(email_code=email_code)

    def accept_privacy_policy_and_terms_of_use(self, ):
        return self.sign_up_controller.accept_privacy_policy_and_terms_of_use_using_post()

    def activate_email(self, email_code: str, pkg_name=None):
        return self.sign_up_controller.activate_email_using_get(email_code=email_code, pkg_name=pkg_name)

    def delete_tenant_account(self, body=None):
        return self.sign_up_controller.delete_tenant_account_using_post(body=body)

    def mobile_login(self, pkg_name: str):
        return self.sign_up_controller.mobile_login_using_get(pkg_name=pkg_name)

    def terms_of_use_accepted(self, ):
        return self.sign_up_controller.terms_of_use_accepted_using_get()

    def is_display_welcome(self, ):
        return self.sign_up_controller.is_display_welcome_using_get()

    def delete_device_v1(self, ):
        return self.trail_controller.delete_device_using_delete1()

    def thing_park_process_request_tpe_delete(self, body: str, request_headers: dict, all_request_params: dict,
                                              routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_delete(body=body,
                                                                                       request_headers=request_headers,
                                                                                       all_request_params=all_request_params,
                                                                                       routing_key=routing_key)

    def thing_park_process_request_tpe_get(self, body: str, request_headers: dict, all_request_params: dict,
                                           routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_get(body=body,
                                                                                    request_headers=request_headers,
                                                                                    all_request_params=all_request_params,
                                                                                    routing_key=routing_key)

    def thing_park_process_request_tpe_head(self, body: str, request_headers: dict, all_request_params: dict,
                                            routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_head(body=body,
                                                                                     request_headers=request_headers,
                                                                                     all_request_params=all_request_params,
                                                                                     routing_key=routing_key)

    def thing_park_process_request_tpe_options(self, body: str, request_headers: dict, all_request_params: dict,
                                               routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_options(body=body,
                                                                                        request_headers=request_headers,
                                                                                        all_request_params=all_request_params,
                                                                                        routing_key=routing_key)

    def thing_park_process_request_tpe_patch(self, body: str, request_headers: dict, all_request_params: dict,
                                             routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_patch(body=body,
                                                                                      request_headers=request_headers,
                                                                                      all_request_params=all_request_params,
                                                                                      routing_key=routing_key)

    def thing_park_process_request_tpe_post(self, body: str, request_headers: dict, all_request_params: dict,
                                            routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_post(body=body,
                                                                                     request_headers=request_headers,
                                                                                     all_request_params=all_request_params,
                                                                                     routing_key=routing_key)

    def thing_park_process_request_tpe_put(self, body: str, request_headers: dict, all_request_params: dict,
                                           routing_key: str):
        return self.thing_park_integration_controller.process_request_tpe_using_put(body=body,
                                                                                    request_headers=request_headers,
                                                                                    all_request_params=all_request_params,
                                                                                    routing_key=routing_key)

    def thing_park_process_request_v5_delete5(self, body: str, request_headers: dict, all_request_params: dict,
                                              routing_key: str):
        return self.thing_park_integration_controller.process_request_using_delete5(body=body,
                                                                                    request_headers=request_headers,
                                                                                    all_request_params=all_request_params,
                                                                                    routing_key=routing_key)

    def thing_park_process_request_v5_get5(self, body: str, request_headers: dict, all_request_params: dict,
                                           routing_key: str):
        return self.thing_park_integration_controller.process_request_using_get5(body=body,
                                                                                 request_headers=request_headers,
                                                                                 all_request_params=all_request_params,
                                                                                 routing_key=routing_key)

    def thing_park_process_request_v5_head5(self, body: str, request_headers: dict, all_request_params: dict,
                                            routing_key: str):
        return self.thing_park_integration_controller.process_request_using_head5(body=body,
                                                                                  request_headers=request_headers,
                                                                                  all_request_params=all_request_params,
                                                                                  routing_key=routing_key)

    def thing_park_process_request_v5_options5(self, body: str, request_headers: dict, all_request_params: dict,
                                               routing_key: str):
        return self.thing_park_integration_controller.process_request_using_options5(body=body,
                                                                                     request_headers=request_headers,
                                                                                     all_request_params=all_request_params,
                                                                                     routing_key=routing_key)

    def thing_park_process_request_v5_patch5(self, body: str, request_headers: dict, all_request_params: dict,
                                             routing_key: str):
        return self.thing_park_integration_controller.process_request_using_patch5(body=body,
                                                                                   request_headers=request_headers,
                                                                                   all_request_params=all_request_params,
                                                                                   routing_key=routing_key)

    def thing_park_process_request_v13_post13(self, body: str, request_headers: dict, all_request_params: dict,
                                              routing_key: str):
        return self.thing_park_integration_controller.process_request_using_post13(body=body,
                                                                                   request_headers=request_headers,
                                                                                   all_request_params=all_request_params,
                                                                                   routing_key=routing_key)

    def thing_park_process_request_v5_put5(self, body: str, request_headers: dict, all_request_params: dict,
                                           routing_key: str):
        return self.thing_park_integration_controller.process_request_using_put5(body=body,
                                                                                 request_headers=request_headers,
                                                                                 all_request_params=all_request_params,
                                                                                 routing_key=routing_key)

    def sig_fox_process_request_v3_delete3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_delete3(body=body,
                                                                                 request_headers=request_headers,
                                                                                 routing_key=routing_key)

    def sig_fox_process_request_v3_get3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_get3(body=body,
                                                                              request_headers=request_headers,
                                                                              routing_key=routing_key)

    def sig_fox_process_request_v3_head3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_head3(body=body,
                                                                               request_headers=request_headers,
                                                                               routing_key=routing_key)

    def sig_fox_process_request_v3_options3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_options3(body=body,
                                                                                  request_headers=request_headers,
                                                                                  routing_key=routing_key)

    def sig_fox_process_request_v3_patch3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_patch3(body=body,
                                                                                request_headers=request_headers,
                                                                                routing_key=routing_key)

    def sig_fox_process_request_v11_post11(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_post11(body=body,
                                                                                request_headers=request_headers,
                                                                                routing_key=routing_key)

    def sig_fox_process_request_v3_put3(self, body: str, request_headers: dict, routing_key: str):
        return self.sig_fox_integration_controller.process_request_using_put3(body=body,
                                                                              request_headers=request_headers,
                                                                              routing_key=routing_key)

    def assign_scheduler_event_to_edge(self, edge_id: EdgeId, scheduler_event_id: SchedulerEventId):
        edge_id = self.get_id(edge_id)
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.assign_scheduler_event_to_edge_using_post(edge_id=edge_id,
                                                                                         scheduler_event_id=scheduler_event_id)

    def delete_scheduler_event(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.delete_scheduler_event_using_delete(
            scheduler_event_id=scheduler_event_id)

    def get_all_scheduler_events(self, edge_id: EdgeId):
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_all_scheduler_events_using_get(edge_id=edge_id)

    def get_edge_scheduler_events(self, edge_id: EdgeId, page_size: int, page: int, text_search=None,
                                  sort_property=None, sort_order=None):
        edge_id = self.get_id(edge_id)
        return self.scheduler_event_controller.get_edge_scheduler_events_using_get(edge_id=edge_id, page_size=page_size,
                                                                                   page=page, text_search=text_search,
                                                                                   sort_property=sort_property,
                                                                                   sort_order=sort_order)

    def get_scheduler_event_by_id(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_by_id_using_get(
            scheduler_event_id=scheduler_event_id)

    def get_scheduler_event_info_by_id(self, scheduler_event_id: SchedulerEventId):
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.get_scheduler_event_info_by_id_using_get(
            scheduler_event_id=scheduler_event_id)

    def get_scheduler_events_by_ids(self, scheduler_event_ids: list):
        return self.scheduler_event_controller.get_scheduler_events_by_ids_using_get(
            scheduler_event_ids=str(scheduler_event_ids))

    def get_scheduler_events(self, type=None):
        return self.scheduler_event_controller.get_scheduler_events_using_get(type=type)

    def save_scheduler_event(self, body=None):
        return self.scheduler_event_controller.save_scheduler_event_using_post(body=body)

    def unassign_scheduler_event_from_edge(self, edge_id: EdgeId, scheduler_event_id: SchedulerEventId):
        edge_id = self.get_id(edge_id)
        scheduler_event_id = self.get_id(scheduler_event_id)
        return self.scheduler_event_controller.unassign_scheduler_event_from_edge_using_delete(edge_id=edge_id,
                                                                                               scheduler_event_id=scheduler_event_id)

    def download_dashboard_report(self, dashboard_id: DashboardId, body=None):
        dashboard_id = self.get_id(dashboard_id)
        return self.report_controller.download_dashboard_report_using_post(dashboard_id=dashboard_id, body=body)

    def download_test_report(self, body=None, reports_server_endpoint_url=None):
        return self.report_controller.download_test_report_using_post(body=body,
                                                                      reports_server_endpoint_url=reports_server_endpoint_url)

    def get_server_time(self, ):
        return self.dashboard_controller.get_server_time_using_get()

    def get_dashboards_by_entity_group_id(self, entity_group_id: EntityGroupId, page_size: int, page: int,
                                          text_search=None, sort_property=None, sort_order=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.get_dashboards_by_entity_group_id_using_get(entity_group_id=entity_group_id,
                                                                                     page_size=page_size, page=page,
                                                                                     text_search=text_search,
                                                                                     sort_property=sort_property,
                                                                                     sort_order=sort_order)

    def get_dashboard_by_id(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_by_id_using_get(dashboard_id=dashboard_id)

    def delete_dashboard(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.delete_dashboard_using_delete(dashboard_id=dashboard_id)

    def save_dashboard(self, body=None, entity_group_id=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.save_dashboard_using_post(body=body, entity_group_id=entity_group_id)

    def get_home_dashboard_info(self, ):
        return self.dashboard_controller.get_home_dashboard_info_using_get()

    def get_tenant_home_dashboard_info(self, ):
        return self.dashboard_controller.get_tenant_home_dashboard_info_using_get()

    def set_customer_home_dashboard_info(self, body=None):
        return self.dashboard_controller.set_customer_home_dashboard_info_using_post(body=body)

    def get_tenant_dashboards_v1(self, tenant_id: TenantId, page_size: int, page: int, text_search=None,
                                 sort_property=None, sort_order=None):
        tenant_id = self.get_id(tenant_id)
        return self.dashboard_controller.get_tenant_dashboards_using_get1(tenant_id=tenant_id, page_size=page_size,
                                                                          page=page, text_search=text_search,
                                                                          sort_property=sort_property,
                                                                          sort_order=sort_order)

    def get_dashboard_info_by_id(self, dashboard_id: DashboardId):
        dashboard_id = self.get_id(dashboard_id)
        return self.dashboard_controller.get_dashboard_info_by_id_using_get(dashboard_id=dashboard_id)

    def get_home_dashboard(self, ):
        return self.dashboard_controller.get_home_dashboard_using_get()

    def get_max_datapoints_limit(self, ):
        return self.dashboard_controller.get_max_datapoints_limit_using_get()

    def get_dashboards_by_ids(self, dashboard_ids: list):
        return self.dashboard_controller.get_dashboards_by_ids_using_get(dashboard_ids=str(dashboard_ids))

    def get_customer_home_dashboard_info(self, ):
        return self.dashboard_controller.get_customer_home_dashboard_info_using_get()

    def get_tenant_dashboards(self, page_size: int, page: int, mobile=None, text_search=None, sort_property=None,
                              sort_order=None):
        return self.dashboard_controller.get_tenant_dashboards_using_get(page_size=page_size, page=page, mobile=mobile,
                                                                         text_search=text_search,
                                                                         sort_property=sort_property,
                                                                         sort_order=sort_order)

    def get_user_dashboards(self, page_size: int, page: int, mobile=None, text_search=None, sort_property=None,
                            sort_order=None, operation=None, user_id=None):
        user_id = self.get_id(user_id)
        return self.dashboard_controller.get_user_dashboards_using_get(page_size=page_size, page=page, mobile=mobile,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order, operation=operation,
                                                                       user_id=user_id)

    def import_group_dashboards(self, entity_group_id: EntityGroupId, body=None, overwrite=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.import_group_dashboards_using_post(entity_group_id=entity_group_id, body=body,
                                                                            overwrite=overwrite)

    def set_tenant_home_dashboard_info(self, body=None):
        return self.dashboard_controller.set_tenant_home_dashboard_info_using_post(body=body)

    def export_group_dashboards(self, entity_group_id: EntityGroupId, limit: int):
        entity_group_id = self.get_id(entity_group_id)
        return self.dashboard_controller.export_group_dashboards_using_get(entity_group_id=entity_group_id, limit=limit)

    def _check_integration_connection_post(self, body=None):
        return self.integration_controller.check_integration_connection_using_post(body=body)

    def _delete_integration_delete(self, integration_id: IntegrationId):
        integration_id = self.get_id(integration_id)
        return self.integration_controller.delete_integration_using_delete(integration_id=integration_id)

    def _get_integration_by_id_get(self, integration_id: IntegrationId):
        integration_id = self.get_id(integration_id)
        return self.integration_controller.get_integration_by_id_using_get(integration_id=integration_id)

    def _get_integration_by_routing_key_get(self, routing_key: str):
        return self.integration_controller.get_integration_by_routing_key_using_get(routing_key=routing_key)

    def _get_integrations_by_ids_get(self, integration_ids: list):
        return self.integration_controller.get_integrations_by_ids_using_get(integration_ids=str(integration_ids))

    def _get_integrations_get(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.integration_controller.get_integrations_using_get(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def _save_integration_post(self, body=None):
        return self.integration_controller.save_integration_using_post(body=body)

    def get_current_custom_menu(self, ):
        return self.custom_menu_controller.get_current_custom_menu_using_get()

    def get_custom_menu(self, ):
        return self.custom_menu_controller.get_custom_menu_using_get()

    def save_custom_menu(self, body=None):
        return self.custom_menu_controller.save_custom_menu_using_post(body=body)

    def get_lwm2m_bootstrap_security_info(self, is_bootstrap_server: bool):
        return self.lwm2m_controller.get_lwm2m_bootstrap_security_info_using_get(
            is_bootstrap_server=is_bootstrap_server)

    def get_current_custom_translation(self, ):
        return self.custom_translation_controller.get_current_custom_translation_using_get()

    def get_custom_translation(self, ):
        return self.custom_translation_controller.get_custom_translation_using_get()

    def save_custom_translation(self, body=None):
        return self.custom_translation_controller.save_custom_translation_using_post(body=body)

    def delete_role(self, role_id: RoleId):
        role_id = self.get_id(role_id)
        return self.role_controller.delete_role_using_delete(role_id=role_id)

    def get_role_by_id(self, role_id: RoleId):
        role_id = self.get_id(role_id)
        return self.role_controller.get_role_by_id_using_get(role_id=role_id)

    def get_roles_by_ids(self, role_ids: list):
        return self.role_controller.get_roles_by_ids_using_get(role_ids=str(role_ids))

    def get_roles(self, page_size: int, page: int, type=None, text_search=None, sort_property=None, sort_order=None):
        return self.role_controller.get_roles_using_get(page_size=page_size, page=page, type=type,
                                                        text_search=text_search, sort_property=sort_property,
                                                        sort_order=sort_order)

    def save_role(self, body=None):
        return self.role_controller.save_role_using_post(body=body)

    def delete_blob_entity(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.delete_blob_entity_using_delete(blob_entity_id=blob_entity_id)

    def download_blob_entity(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.download_blob_entity_using_get(blob_entity_id=blob_entity_id)

    def get_blob_entities_by_ids(self, blob_entity_ids: list):
        return self.blob_entity_controller.get_blob_entities_by_ids_using_get(blob_entity_ids=str(blob_entity_ids))

    def get_blob_entities(self, page_size: int, page: int, type=None, text_search=None, sort_property=None,
                          sort_order=None, start_time=None, end_time=None):
        return self.blob_entity_controller.get_blob_entities_using_get(page_size=page_size, page=page, type=type,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order, start_time=start_time,
                                                                       end_time=end_time)

    def get_blob_entity_info_by_id(self, blob_entity_id: BlobEntityId):
        blob_entity_id = self.get_id(blob_entity_id)
        return self.blob_entity_controller.get_blob_entity_info_by_id_using_get(blob_entity_id=blob_entity_id)

    def loriot_process_request_v1_delete1(self, body: str, request_headers: dict, routing_key: str):
        return self.loriot_integration_controller.process_request_using_delete1(body=body,
                                                                                request_headers=request_headers,
                                                                                routing_key=routing_key)

    def loriot_process_request_v1_get1(self, body: str, request_headers: dict, routing_key: str):
        return self.loriot_integration_controller.process_request_using_get1(body=body, request_headers=request_headers,
                                                                             routing_key=routing_key)

    def loriot_process_request_v1_head1(self, body: str, request_headers: dict, routing_key: str):
        return self.loriot_integration_controller.process_request_using_head1(body=body,
                                                                              request_headers=request_headers,
                                                                              routing_key=routing_key)

    def loriot_process_request_v1_options1(self, body: str, request_headers: dict, routing_key: str):
        return self.loriot_integration_controller.process_request_using_options1(body=body,
                                                                                 request_headers=request_headers,
                                                                                 routing_key=routing_key)

    def loriot_process_request_v1_patch1(self, body: str, request_headers: dict, routing_key: str):
        return self.loriot_integration_controller.process_request_using_patch1(body=body,
                                                                               request_headers=request_headers,
                                                                               routing_key=routing_key)

    def loriot_process_request_v9_post9(self, body: str, request_headers: dict, routing_key: str):
        return self.loriot_integration_controller.process_request_using_post9(body=body,
                                                                              request_headers=request_headers,
                                                                              routing_key=routing_key)

    def loriot_process_request_v1_put1(self, body: str, request_headers: dict, routing_key: str):
        return self.loriot_integration_controller.process_request_using_put1(body=body, request_headers=request_headers,
                                                                             routing_key=routing_key)

    def get_tenant_infos(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.tenant_controller.get_tenant_infos_using_get(page_size=page_size, page=page,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def get_tenant_by_id(self, tenant_id: TenantId):
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_by_id_using_get(tenant_id=tenant_id)

    def save_tenant(self, body=None):
        return self.tenant_controller.save_tenant_using_post(body=body)

    def get_tenants(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.tenant_controller.get_tenants_using_get(page_size=page_size, page=page, text_search=text_search,
                                                            sort_property=sort_property, sort_order=sort_order)

    def get_tenants_by_ids(self, tenant_ids: list):
        return self.tenant_controller.get_tenants_by_ids_using_get(tenant_ids=str(tenant_ids))

    def get_tenant_info_by_id(self, tenant_id: TenantId):
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.get_tenant_info_by_id_using_get(tenant_id=tenant_id)

    def delete_tenant(self, tenant_id: TenantId):
        tenant_id = self.get_id(tenant_id)
        return self.tenant_controller.delete_tenant_using_delete(tenant_id=tenant_id)

    def chirp_stack_process_request_delete(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_delete(body=body,
                                                                                    request_headers=request_headers,
                                                                                    routing_key=routing_key)

    def chirp_stack_process_request_get(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_get(body=body,
                                                                                 request_headers=request_headers,
                                                                                 routing_key=routing_key)

    def chirp_stack_process_request_head(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_head(body=body,
                                                                                  request_headers=request_headers,
                                                                                  routing_key=routing_key)

    def chirp_stack_process_request_options(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_options(body=body,
                                                                                     request_headers=request_headers,
                                                                                     routing_key=routing_key)

    def chirp_stack_process_request_patch(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_patch(body=body,
                                                                                   request_headers=request_headers,
                                                                                   routing_key=routing_key)

    def chirp_stack_process_request_post(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_post(body=body,
                                                                                  request_headers=request_headers,
                                                                                  routing_key=routing_key)

    def chirp_stack_process_request_put(self, body: str, request_headers: dict, routing_key: str):
        return self.chirp_stack_integration_controller.process_request_using_put(body=body,
                                                                                 request_headers=request_headers,
                                                                                 routing_key=routing_key)

    def get_app_theme_css(self, body=None):
        return self.white_labeling_controller.get_app_theme_css_using_post(body=body)

    def get_current_login_white_label_params(self, ):
        return self.white_labeling_controller.get_current_login_white_label_params_using_get()

    def get_current_white_label_params(self, ):
        return self.white_labeling_controller.get_current_white_label_params_using_get()

    def get_login_theme_css(self, body=None, dark_foreground=None):
        return self.white_labeling_controller.get_login_theme_css_using_post(body=body, dark_foreground=dark_foreground)

    def get_login_white_label_params(self, logo_image_checksum: str, favicon_checksum: str):
        return self.white_labeling_controller.get_login_white_label_params_using_get(
            logo_image_checksum=logo_image_checksum, favicon_checksum=favicon_checksum)

    def get_white_label_params(self, logo_image_checksum: str, favicon_checksum: str):
        return self.white_labeling_controller.get_white_label_params_using_get(logo_image_checksum=logo_image_checksum,
                                                                               favicon_checksum=favicon_checksum)

    def is_customer_white_labeling_allowed(self, ):
        return self.white_labeling_controller.is_customer_white_labeling_allowed_using_get()

    def is_white_labeling_allowed(self, ):
        return self.white_labeling_controller.is_white_labeling_allowed_using_get()

    def preview_white_label_params(self, body=None):
        return self.white_labeling_controller.preview_white_label_params_using_post(body=body)

    def save_login_white_label_params(self, body=None):
        return self.white_labeling_controller.save_login_white_label_params_using_post(body=body)

    def save_white_label_params(self, body=None):
        return self.white_labeling_controller.save_white_label_params_using_post(body=body)

    def tenant_white_labeling_allowed(self, ):
        return self.white_labeling_controller.tenant_white_labeling_allowed_using_get()

    def delete_ota_package(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.delete_ota_package_using_delete(ota_package_id=ota_package_id)

    def get_ota_packages_v1(self, device_profile_id: DeviceProfileId, type: str, page_size: int, page: int,
                            text_search=None, sort_property=None, sort_order=None):
        device_profile_id = self.get_id(device_profile_id)
        return self.ota_package_controller.get_ota_packages_using_get1(device_profile_id=device_profile_id, type=type,
                                                                       page_size=page_size, page=page,
                                                                       text_search=text_search,
                                                                       sort_property=sort_property,
                                                                       sort_order=sort_order)

    def save_ota_package_data(self, checksum_algorithm: str, ota_package_id: OtaPackageId, body=None, checksum=None):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.save_ota_package_data_using_post(checksum_algorithm=checksum_algorithm,
                                                                            ota_package_id=ota_package_id, body=body,
                                                                            checksum=checksum)

    def save_ota_package_info(self, body=None):
        return self.ota_package_controller.save_ota_package_info_using_post(body=body)

    def get_ota_packages(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.ota_package_controller.get_ota_packages_using_get(page_size=page_size, page=page,
                                                                      text_search=text_search,
                                                                      sort_property=sort_property,
                                                                      sort_order=sort_order)

    def get_ota_package_by_id(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_by_id_using_get(ota_package_id=ota_package_id)

    def get_group_ota_packages(self, group_id: EntityGroupId, type: str, page_size: int, page: int, text_search=None,
                               sort_property=None, sort_order=None):
        group_id = self.get_id(group_id)
        return self.ota_package_controller.get_group_ota_packages_using_get(group_id=group_id, type=type,
                                                                            page_size=page_size, page=page,
                                                                            text_search=text_search,
                                                                            sort_property=sort_property,
                                                                            sort_order=sort_order)

    def download_ota_package(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.download_ota_package_using_get(ota_package_id=ota_package_id)

    def get_ota_package_info_by_id(self, ota_package_id: OtaPackageId):
        ota_package_id = self.get_id(ota_package_id)
        return self.ota_package_controller.get_ota_package_info_by_id_using_get(ota_package_id=ota_package_id)

    def add_entities_to_entity_group(self, entity_group_id: EntityGroupId, body=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.add_entities_to_entity_group_using_post(entity_group_id=entity_group_id,
                                                                                    body=body)

    def assign_entity_group_to_edge(self, edge_id: EdgeId, group_type: str, entity_group_id: EntityGroupId):
        edge_id = self.get_id(edge_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.assign_entity_group_to_edge_using_post(edge_id=edge_id,
                                                                                   group_type=group_type,
                                                                                   entity_group_id=entity_group_id)

    def delete_entity_group(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.delete_entity_group_using_delete(entity_group_id=entity_group_id)

    def get_all_edge_entity_groups(self, edge_id: EdgeId, group_type: str):
        edge_id = self.get_id(edge_id)
        return self.entity_group_controller.get_all_edge_entity_groups_using_get(edge_id=edge_id, group_type=group_type)

    def get_edge_entity_groups(self, edge_id: EdgeId, group_type: str, page_size: int, page: int, sort_property=None,
                               sort_order=None):
        edge_id = self.get_id(edge_id)
        return self.entity_group_controller.get_edge_entity_groups_using_get(edge_id=edge_id, group_type=group_type,
                                                                             page_size=page_size, page=page,
                                                                             sort_property=sort_property,
                                                                             sort_order=sort_order)

    def get_entities(self, entity_group_id: EntityGroupId, page_size: int, page: int, text_search=None,
                     sort_property=None, sort_order=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entities_using_get(entity_group_id=entity_group_id, page_size=page_size,
                                                                   page=page, text_search=text_search,
                                                                   sort_property=sort_property, sort_order=sort_order)

    def get_entity_group_all_by_owner_and_type(self, owner_type: str, owner_id: UserId, group_type: str):
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_group_all_by_owner_and_type_using_get(owner_type=owner_type,
                                                                                             owner_id=owner_id,
                                                                                             group_type=group_type)

    def get_entity_group_by_id(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.get_entity_group_by_id_using_get(entity_group_id=entity_group_id)

    def get_entity_group_by_owner_and_name_and_type(self, owner_type: str, owner_id: UserId, group_type: str,
                                                    group_name: str):
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_group_by_owner_and_name_and_type_using_get(owner_type=owner_type,
                                                                                                  owner_id=owner_id,
                                                                                                  group_type=group_type,
                                                                                                  group_name=group_name)

    def get_entity_groups_by_ids(self, entity_group_ids: list):
        return self.entity_group_controller.get_entity_groups_by_ids_using_get(entity_group_ids=str(entity_group_ids))

    def get_entity_groups_by_owner_and_type(self, owner_type: str, owner_id: UserId, group_type: str):
        owner_id = self.get_id(owner_id)
        return self.entity_group_controller.get_entity_groups_by_owner_and_type_using_get(owner_type=owner_type,
                                                                                          owner_id=owner_id,
                                                                                          group_type=group_type)

    def get_entity_groups_by_type(self, group_type: str):
        return self.entity_group_controller.get_entity_groups_by_type_using_get(group_type=group_type)

    def get_entity_groups_for_entity(self, entity_type: str, entity_id: EntityId):
        entity_id = self.get_id(entity_id)
        return self.entity_group_controller.get_entity_groups_for_entity_using_get(entity_type=entity_type,
                                                                                   entity_id=entity_id)

    def get_group_entity(self, entity_group_id: EntityGroupId, entity_id: EntityId):
        entity_group_id = self.get_id(entity_group_id)
        entity_id = self.get_id(entity_id)
        return self.entity_group_controller.get_group_entity_using_get(entity_group_id=entity_group_id,
                                                                       entity_id=entity_id)

    def get_owners(self, page_size: int, page: int, text_search=None, sort_property=None, sort_order=None):
        return self.entity_group_controller.get_owners_using_get(page_size=page_size, page=page,
                                                                 text_search=text_search, sort_property=sort_property,
                                                                 sort_order=sort_order)

    def make_entity_group_private(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.make_entity_group_private_using_post(entity_group_id=entity_group_id)

    def make_entity_group_public(self, entity_group_id: EntityGroupId):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.make_entity_group_public_using_post(entity_group_id=entity_group_id)

    def remove_entities_from_entity_group(self, entity_group_id: EntityGroupId, body=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.remove_entities_from_entity_group_using_post(
            entity_group_id=entity_group_id, body=body)

    def save_entity_group(self, body=None):
        return self.entity_group_controller.save_entity_group_using_post(body=body)

    def share_entity_group_to_child_owner_user_group(self, entity_group_id: EntityGroupId, user_group_id: EntityId,
                                                     role_id: RoleId):
        entity_group_id = self.get_id(entity_group_id)
        user_group_id = self.get_id(user_group_id)
        role_id = self.get_id(role_id)
        return self.entity_group_controller.share_entity_group_to_child_owner_user_group_using_post(
            entity_group_id=entity_group_id, user_group_id=user_group_id, role_id=role_id)

    def share_entity_group(self, entity_group_id: EntityGroupId, body=None):
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.share_entity_group_using_post(entity_group_id=entity_group_id, body=body)

    def unassign_entity_group_from_edge(self, edge_id: EdgeId, group_type: str, entity_group_id: EntityGroupId):
        edge_id = self.get_id(edge_id)
        entity_group_id = self.get_id(entity_group_id)
        return self.entity_group_controller.unassign_entity_group_from_edge_using_delete(edge_id=edge_id,
                                                                                         group_type=group_type,
                                                                                         entity_group_id=entity_group_id)

    # Subscription Controller
    def get_tenant_profile_data_by_id(self, tenant_profile_id: TenantProfileId):
        tenant_profile_id = self.get_id(tenant_profile_id)
        return self.subscription_controller.get_tenant_profile_data_by_id_using_get(tenant_profile_id=tenant_profile_id)

    def get_tenant_profile_data(self, ):
        return self.subscription_controller.get_tenant_profile_data_using_get()

    def get_tenant_subscription_usage(self):
        return self.subscription_controller.get_tenant_subscription_usage_using_get()

    # Solution Controller
    def get_solution_template_details(self, solution_template_id):
        return self.solution_controller.get_solution_template_details_using_get(
            solution_template_id=solution_template_id)

    def get_solution_template_infos(self):
        return self.solution_controller.get_solution_template_infos_using_get()

    def get_solution_template_instructions(self, solution_template_id):
        return self.solution_controller.get_solution_template_instructions_using_get(
            solution_template_id=solution_template_id)

    def install_solution_template(self, solution_template_id):
        return self.solution_controller.install_solution_template_using_post(solution_template_id=solution_template_id)

    def uninstall_solution_template(self, solution_template_id):
        return self.solution_controller.uninstall_solution_template_using_delete(
            solution_template_id=solution_template_id)

    def __load_controllers(self):
        self.http_integration_controller = HttpIntegrationControllerApi(self.api_client)
        self.user_permissions_controller = UserPermissionsControllerApi(self.api_client)
        self.device_group_ota_package_controller = DeviceGroupOtaPackageControllerApi(self.api_client)
        self.converter_controller = ConverterControllerApi(self.api_client)
        self.t_mobile_iot_cdp_integration_controller = TMobileIotCdpIntegrationControllerApi(self.api_client)
        self.customer_controller = CustomerControllerApi(self.api_client)
        self.role_controller = RoleControllerApi(self.api_client)
        self.entity_group_controller = EntityGroupControllerApi(self.api_client)
        self.admin_controller = AdminControllerApi(self.api_client)
        self.edge_controller = EdgeControllerApi(self.api_client)
        self.tenant_controller = TenantControllerApi(self.api_client)
        self.trail_controller = TrailControllerApi(self.api_client)
        self.report_controller = ReportControllerApi(self.api_client)
        self.dashboard_controller = DashboardControllerApi(self.api_client)
        self.loriot_integration_controller = LoriotIntegrationControllerApi(self.api_client)
        self.entity_view_controller = EntityViewControllerApi(self.api_client)
        self.rpc_v2_controller = RpcV2ControllerApi(self.api_client)
        self.lwm2m_controller = Lwm2mControllerApi(self.api_client)
        self.scheduler_event_controller = SchedulerEventControllerApi(self.api_client)
        self.custom_menu_controller = CustomMenuControllerApi(self.api_client)
        self.thing_park_integration_controller = ThingParkIntegrationControllerApi(self.api_client)
        self.rule_engine_controller = RuleEngineControllerApi(self.api_client)
        self.ocean_connect_integration_controller = OceanConnectIntegrationControllerApi(self.api_client)
        self.integration_controller = IntegrationControllerApi(self.api_client)
        self.custom_translation_controller = CustomTranslationControllerApi(self.api_client)
        self.ota_package_controller = OtaPackageControllerApi(self.api_client)
        self.edge_event_controller = EdgeEventControllerApi(self.api_client)
        self.device_controller = DeviceControllerApi(self.api_client)
        self.group_permission_controller = GroupPermissionControllerApi(self.api_client)
        self.chirp_stack_integration_controller = ChirpStackIntegrationControllerApi(self.api_client)
        self.user_controller = UserControllerApi(self.api_client)
        self.white_labeling_controller = WhiteLabelingControllerApi(self.api_client)
        self.sign_up_controller = SignUpControllerApi(self.api_client)
        self.blob_entity_controller = BlobEntityControllerApi(self.api_client)
        self.owner_controller = OwnerControllerApi(self.api_client)
        self.self_registration_controller = SelfRegistrationControllerApi(self.api_client)
        self.sig_fox_integration_controller = SigFoxIntegrationControllerApi(self.api_client)
        self.asset_controller = AssetControllerApi(self.api_client)
        self.subscription_controller = SubscriptionControllerApi(self.api_client)
        self.solution_controller = SolutionControllerApi(self.api_client)
