# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


class VRSRole(object):
    """ VRSRole """

    MASTER = u"MASTER"
    NONE = u"NONE"
    SLAVE = u"SLAVE"
    

class IngressACLEntryTemplateAssociatedApplicationObjectType(object):
    """ IngressACLEntryTemplateAssociatedApplicationObjectType """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class InfrastructureGatewayProfileSystemSyncWindow(object):
    """ InfrastructureGatewayProfileSystemSyncWindow """

    TEN_MINUTES = u"TEN_MINUTES"
    NONE = u"NONE"
    TWO_HOURS = u"TWO_HOURS"
    ONE_HOUR = u"ONE_HOUR"
    SIX_HOURS = u"SIX_HOURS"
    THREE_HOURS = u"THREE_HOURS"
    FOUR_HOURS = u"FOUR_HOURS"
    THIRTY_MINUTES = u"THIRTY_MINUTES"
    MAXIMUM_DURATION = u"MAXIMUM_DURATION"
    FIVE_HOURS = u"FIVE_HOURS"
    

class DomainDHCPBehavior(object):
    """ DomainDHCPBehavior """

    FLOOD = u"FLOOD"
    CONSUME = u"CONSUME"
    RELAY = u"RELAY"
    

class DomainUplinkPreference(object):
    """ DomainUplinkPreference """

    SYMMETRIC = u"SYMMETRIC"
    PRIMARY_SECONDARY = u"PRIMARY_SECONDARY"
    SECONDARY_PRIMARY = u"SECONDARY_PRIMARY"
    PRIMARY = u"PRIMARY"
    SECONDARY = u"SECONDARY"
    

class TCAType(object):
    """ TCAType """

    ROLLING_AVERAGE = u"ROLLING_AVERAGE"
    BREACH = u"BREACH"
    

class TCAMetric(object):
    """ TCAMetric """

    INGRESS_BYTE_COUNT = u"INGRESS_BYTE_COUNT"
    PACKETS_OUT = u"PACKETS_OUT"
    PACKETS_OUT_DROPPED = u"PACKETS_OUT_DROPPED"
    PACKETS_IN_ERROR = u"PACKETS_IN_ERROR"
    BYTES_IN = u"BYTES_IN"
    EGRESS_PACKET_COUNT = u"EGRESS_PACKET_COUNT"
    PACKETS_OUT_ERROR = u"PACKETS_OUT_ERROR"
    PACKETS_IN_DROPPED = u"PACKETS_IN_DROPPED"
    EGRESS_BYTE_COUNT = u"EGRESS_BYTE_COUNT"
    BYTES_OUT = u"BYTES_OUT"
    INGRESS_PACKET_COUNT = u"INGRESS_PACKET_COUNT"
    PACKETS_DROPPED_BY_RATE_LIMIT = u"PACKETS_DROPPED_BY_RATE_LIMIT"
    PACKETS_IN = u"PACKETS_IN"
    

class EnterpriseProfileEncryptionManagementMode(object):
    """ EnterpriseProfileEncryptionManagementMode """

    DISABLED = u"DISABLED"
    MANAGED = u"MANAGED"
    

class KeyServerMonitorSeedSeedTrafficEncryptionAlgorithm(object):
    """ KeyServerMonitorSeedSeedTrafficEncryptionAlgorithm """

    AES_192_CBC = u"AES_192_CBC"
    TRIPLE_DES_CBC = u"TRIPLE_DES_CBC"
    AES_256_CBC = u"AES_256_CBC"
    AES_128_CBC = u"AES_128_CBC"
    

class UplinkRDUplinkType(object):
    """ UplinkRDUplinkType """

    RD_SECONDARY2 = u"RD_SECONDARY2"
    RD_PRIMARY1 = u"RD_PRIMARY1"
    RD_PRIMARY2 = u"RD_PRIMARY2"
    RD_SECONDARY1 = u"RD_SECONDARY1"
    

class VRSStatus(object):
    """ VRSStatus """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class EgressACLEntryTemplateNetworkType(object):
    """ EgressACLEntryTemplateNetworkType """

    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ENDPOINT_DOMAIN = u"ENDPOINT_DOMAIN"
    ZONE = u"ZONE"
    ENDPOINT_ZONE = u"ENDPOINT_ZONE"
    NETWORK_MACRO_GROUP = u"NETWORK_MACRO_GROUP"
    ENDPOINT_SUBNET = u"ENDPOINT_SUBNET"
    INTERNET_POLICYGROUP = u"INTERNET_POLICYGROUP"
    PUBLIC_NETWORK = u"PUBLIC_NETWORK"
    ENTERPRISE_NETWORK = u"ENTERPRISE_NETWORK"
    ANY = u"ANY"
    

class SystemConfigGroupKeyDefaultSeedPayloadSigningAlgorithm(object):
    """ SystemConfigGroupKeyDefaultSeedPayloadSigningAlgorithm """

    SHA256WITHRSA = u"SHA256WITHRSA"
    SHA384WITHRSA = u"SHA384WITHRSA"
    SHA1WITHRSA = u"SHA1WITHRSA"
    SHA512WITHRSA = u"SHA512WITHRSA"
    SHA224WITHRSA = u"SHA224WITHRSA"
    

class IngressACLEntryTemplatePolicyState(object):
    """ IngressACLEntryTemplatePolicyState """

    LIVE = u"LIVE"
    DRAFT = u"DRAFT"
    

class DomainTemplateEncryption(object):
    """ DomainTemplateEncryption """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    

class GroupKeyEncryptionProfileSEKPayloadSigningAlgorithm(object):
    """ GroupKeyEncryptionProfileSEKPayloadSigningAlgorithm """

    SHA256WITHRSA = u"SHA256WITHRSA"
    SHA384WITHRSA = u"SHA384WITHRSA"
    SHA1WITHRSA = u"SHA1WITHRSA"
    SHA512WITHRSA = u"SHA512WITHRSA"
    SHA224WITHRSA = u"SHA224WITHRSA"
    

class JobCommand(object):
    """ JobCommand """

    NOTIFY_NSG_REGISTRATION = u"NOTIFY_NSG_REGISTRATION"
    RELOAD_NSG_CONFIG = u"RELOAD_NSG_CONFIG"
    FORCE_KEYSERVER_UPDATE_ACK = u"FORCE_KEYSERVER_UPDATE_ACK"
    VCENTER_RELOAD = u"VCENTER_RELOAD"
    KEYSERVER_NOTIFICATION_TEST = u"KEYSERVER_NOTIFICATION_TEST"
    EXPORT = u"EXPORT"
    FORCE_KEYSERVER_VSD_RESYNC = u"FORCE_KEYSERVER_VSD_RESYNC"
    RELOAD_GEO_REDUNDANT_INFO = u"RELOAD_GEO_REDUNDANT_INFO"
    CERTIFICATE_NSG_REVOKE = u"CERTIFICATE_NSG_REVOKE"
    BEGIN_POLICY_CHANGES = u"BEGIN_POLICY_CHANGES"
    IMPORT = u"IMPORT"
    APPLY_POLICY_CHANGES = u"APPLY_POLICY_CHANGES"
    NSG_NOTIFICATION_TEST = u"NSG_NOTIFICATION_TEST"
    DISCARD_POLICY_CHANGES = u"DISCARD_POLICY_CHANGES"
    NSG_REGISTRATION_INFO = u"NSG_REGISTRATION_INFO"
    NOTIFY_NSG_REGISTRATION_ACK = u"NOTIFY_NSG_REGISTRATION_ACK"
    NOTIFY_NSG_REGISTRATION_TEST = u"NOTIFY_NSG_REGISTRATION_TEST"
    CERTIFICATE_NSG_RENEW = u"CERTIFICATE_NSG_RENEW"
    FORCE_KEYSERVER_UPDATE = u"FORCE_KEYSERVER_UPDATE"
    BATCH_CRUD_REQUEST = u"BATCH_CRUD_REQUEST"
    RELOAD = u"RELOAD"
    GATEWAY_AUDIT = u"GATEWAY_AUDIT"
    

class DomainEncryption(object):
    """ DomainEncryption """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    

class InfrastructureGatewayProfileDeadTimer(object):
    """ InfrastructureGatewayProfileDeadTimer """

    TEN_MINUTES = u"TEN_MINUTES"
    NONE = u"NONE"
    TWO_HOURS = u"TWO_HOURS"
    ONE_HOUR = u"ONE_HOUR"
    SIX_HOURS = u"SIX_HOURS"
    THREE_HOURS = u"THREE_HOURS"
    FOUR_HOURS = u"FOUR_HOURS"
    THIRTY_MINUTES = u"THIRTY_MINUTES"
    MAXIMUM_DURATION = u"MAXIMUM_DURATION"
    FIVE_HOURS = u"FIVE_HOURS"
    

class VRSJSONRPCConnectionState(object):
    """ VRSJSONRPCConnectionState """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class PortTemplatePortType(object):
    """ PortTemplatePortType """

    ACCESS = u"ACCESS"
    NETWORK = u"NETWORK"
    

class VPortMirrorMirrorDirection(object):
    """ VPortMirrorMirrorDirection """

    BOTH = u"BOTH"
    INGRESS = u"INGRESS"
    EGRESS = u"EGRESS"
    

class SubnetTemplateEncryption(object):
    """ SubnetTemplateEncryption """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class IngressExternalServiceTemplateEntryAction(object):
    """ IngressExternalServiceTemplateEntryAction """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class HSCType(object):
    """ HSCType """

    VSA = u"VSA"
    NONE = u"NONE"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    

class RESTUserAvatarType(object):
    """ RESTUserAvatarType """

    URL = u"URL"
    COMPUTEDURL = u"COMPUTEDURL"
    BASE64 = u"BASE64"
    

class DomainPolicyChangeStatus(object):
    """ DomainPolicyChangeStatus """

    USE = u"USE"
    EXTEND = u"EXTEND"
    DEPLOY = u"DEPLOY"
    READ = u"READ"
    INSTANTIATE = u"INSTANTIATE"
    ALL = u"ALL"
    

class DomainApplicationDeploymentPolicy(object):
    """ DomainApplicationDeploymentPolicy """

    NONE = u"NONE"
    ZONE = u"ZONE"
    

class HSCStatus(object):
    """ HSCStatus """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class VRSPersonality(object):
    """ VRSPersonality """

    VRS = u"VRS"
    VRSG = u"VRSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    NONE = u"NONE"
    NSG = u"NSG"
    

class PortStatus(object):
    """ PortStatus """

    READY = u"READY"
    MISMATCH = u"MISMATCH"
    ORPHAN = u"ORPHAN"
    INITIALIZED = u"INITIALIZED"
    

class InfrastructurePortProfileDuplex(object):
    """ InfrastructurePortProfileDuplex """

    FULL = u"FULL"
    SIMPLEX = u"SIMPLEX"
    HALF = u"HALF"
    

class ZoneTemplateEncryption(object):
    """ ZoneTemplateEncryption """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class GatewayPersonality(object):
    """ GatewayPersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class RedirectionTargetEndPointType(object):
    """ RedirectionTargetEndPointType """

    NONE = u"NONE"
    L3 = u"L3"
    VIRTUAL_WIRE = u"VIRTUAL_WIRE"
    

class EgressACLEntryTemplatePolicyState(object):
    """ EgressACLEntryTemplatePolicyState """

    LIVE = u"LIVE"
    DRAFT = u"DRAFT"
    

class PolicyGroupTemplateType(object):
    """ PolicyGroupTemplateType """

    HARDWARE = u"HARDWARE"
    SOFTWARE = u"SOFTWARE"
    

class SystemConfigGroupKeyDefaultTrafficAuthenticationAlgorithm(object):
    """ SystemConfigGroupKeyDefaultTrafficAuthenticationAlgorithm """

    HMAC_MD5 = u"HMAC_MD5"
    HMAC_SHA256 = u"HMAC_SHA256"
    HMAC_SHA1 = u"HMAC_SHA1"
    HMAC_SHA512 = u"HMAC_SHA512"
    HMAC_SHA384 = u"HMAC_SHA384"
    

class IngressExternalServiceTemplateEntryLocationType(object):
    """ IngressExternalServiceTemplateEntryLocationType """

    VPORTTAG = u"VPORTTAG"
    REDIRECTIONTARGET = u"REDIRECTIONTARGET"
    ZONE = u"ZONE"
    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ANY = u"ANY"
    

class VRSHypervisorConnectionState(object):
    """ VRSHypervisorConnectionState """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class NSRedundantGWGrpPersonality(object):
    """ NSRedundantGWGrpPersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class TCAScope(object):
    """ TCAScope """

    GLOBAL = u"GLOBAL"
    LOCAL = u"LOCAL"
    

class EgressQOSPolicyQueue3ForwardingClasses(object):
    """ EgressQOSPolicyQueue3ForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class RedundantPortPortType(object):
    """ RedundantPortPortType """

    ACCESS = u"ACCESS"
    NETWORK = u"NETWORK"
    

class GroupKeyEncryptionProfileSeedPayloadSigningAlgorithm(object):
    """ GroupKeyEncryptionProfileSeedPayloadSigningAlgorithm """

    SHA256WITHRSA = u"SHA256WITHRSA"
    SHA384WITHRSA = u"SHA384WITHRSA"
    SHA1WITHRSA = u"SHA1WITHRSA"
    SHA512WITHRSA = u"SHA512WITHRSA"
    SHA224WITHRSA = u"SHA224WITHRSA"
    

class TierType(object):
    """ TierType """

    APPLICATION_EXTENDED_NETWORK = u"APPLICATION_EXTENDED_NETWORK"
    APPLICATION = u"APPLICATION"
    NETWORK_MACRO = u"NETWORK_MACRO"
    STANDARD = u"STANDARD"
    

class UserAvatarType(object):
    """ UserAvatarType """

    URL = u"URL"
    COMPUTEDURL = u"COMPUTEDURL"
    BASE64 = u"BASE64"
    

class InfrastructurePortProfileUplinkTag(object):
    """ InfrastructurePortProfileUplinkTag """

    UNKNOWN = u"UNKNOWN"
    PRIMARY = u"PRIMARY"
    TERTIARY = u"TERTIARY"
    SECONDARY = u"SECONDARY"
    

class RedundantPortStatus(object):
    """ RedundantPortStatus """

    READY = u"READY"
    MISMATCH = u"MISMATCH"
    ORPHAN = u"ORPHAN"
    INITIALIZED = u"INITIALIZED"
    

class SubnetEncryption(object):
    """ SubnetEncryption """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class VMStatus(object):
    """ VMStatus """

    INIT = u"INIT"
    LAST = u"LAST"
    NOSTATE = u"NOSTATE"
    UNKNOWN = u"UNKNOWN"
    SHUTOFF = u"SHUTOFF"
    PAUSED = u"PAUSED"
    CRASHED = u"CRASHED"
    RUNNING = u"RUNNING"
    DELETE_PENDING = u"DELETE_PENDING"
    SHUTDOWN = u"SHUTDOWN"
    UNREACHABLE = u"UNREACHABLE"
    BLOCKED = u"BLOCKED"
    

class VMReasonType(object):
    """ VMReasonType """

    PAUSED_DUMP = u"PAUSED_DUMP"
    SHUTOFF_UNKNOWN = u"SHUTOFF_UNKNOWN"
    PAUSED_MIGRATION = u"PAUSED_MIGRATION"
    SHUTOFF_DESTROYED = u"SHUTOFF_DESTROYED"
    UNKNOWN = u"UNKNOWN"
    PAUSED_SHUTTING_DOWN = u"PAUSED_SHUTTING_DOWN"
    SHUTOFF_FROM_SNAPSHOT = u"SHUTOFF_FROM_SNAPSHOT"
    RUNNING_MIGRATED = u"RUNNING_MIGRATED"
    CRASHED_UNKNOWN = u"CRASHED_UNKNOWN"
    PAUSED_SAVE = u"PAUSED_SAVE"
    RUNNING_RESTORED = u"RUNNING_RESTORED"
    SHUTDOWN_USER = u"SHUTDOWN_USER"
    RUNNING_LAST = u"RUNNING_LAST"
    SHUTOFF_LAST = u"SHUTOFF_LAST"
    SHUTDOWN_UNKNOWN = u"SHUTDOWN_UNKNOWN"
    RUNNING_MIGRATION_CANCELED = u"RUNNING_MIGRATION_CANCELED"
    PAUSED_LAST = u"PAUSED_LAST"
    NOSTATE_UNKNOWN = u"NOSTATE_UNKNOWN"
    PAUSED_UNKNOWN = u"PAUSED_UNKNOWN"
    RUNNING_BOOTED = u"RUNNING_BOOTED"
    RUNNING_UNKNOWN = u"RUNNING_UNKNOWN"
    PAUSED_USER = u"PAUSED_USER"
    CRASHED_LAST = u"CRASHED_LAST"
    RUNNING_FROM_SNAPSHOT = u"RUNNING_FROM_SNAPSHOT"
    SHUTOFF_SHUTDOWN = u"SHUTOFF_SHUTDOWN"
    SHUTOFF_CRASHED = u"SHUTOFF_CRASHED"
    SHUTOFF_MIGRATED = u"SHUTOFF_MIGRATED"
    RUNNING_SAVE_CANCELED = u"RUNNING_SAVE_CANCELED"
    RUNNING_UNPAUSED = u"RUNNING_UNPAUSED"
    PAUSED_IOERROR = u"PAUSED_IOERROR"
    PAUSED_FROM_SNAPSHOT = u"PAUSED_FROM_SNAPSHOT"
    BLOCKED_LAST = u"BLOCKED_LAST"
    SHUTOFF_SAVED = u"SHUTOFF_SAVED"
    NOSTATE_LAST = u"NOSTATE_LAST"
    SHUTDOWN_LAST = u"SHUTDOWN_LAST"
    SHUTOFF_FAILED = u"SHUTOFF_FAILED"
    PAUSED_WATCHDOG = u"PAUSED_WATCHDOG"
    BLOCKED_UNKNOWN = u"BLOCKED_UNKNOWN"
    

class MonitoringPortState(object):
    """ MonitoringPortState """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class InfrastructureGatewayProfileUpgradeAction(object):
    """ InfrastructureGatewayProfileUpgradeAction """

    DOWNLOAD_AND_UPGRADE_AT_WINDOW = u"DOWNLOAD_AND_UPGRADE_AT_WINDOW"
    UPGRADE_AT_BOOTSTRAPPING = u"UPGRADE_AT_BOOTSTRAPPING"
    NONE = u"NONE"
    DOWNLOAD_ONLY = u"DOWNLOAD_ONLY"
    UPGRADE_NOW = u"UPGRADE_NOW"
    DOWNLOAD_AND_UPGRADE_NOW = u"DOWNLOAD_AND_UPGRADE_NOW"
    

class WANServiceTunnelType(object):
    """ WANServiceTunnelType """

    DC_DEFAULT = u"DC_DEFAULT"
    VXLAN = u"VXLAN"
    GRE = u"GRE"
    

class GroupKeyEncryptionProfileTrafficEncryptionAlgorithm(object):
    """ GroupKeyEncryptionProfileTrafficEncryptionAlgorithm """

    AES_192_CBC = u"AES_192_CBC"
    TRIPLE_DES_CBC = u"TRIPLE_DES_CBC"
    AES_256_CBC = u"AES_256_CBC"
    AES_128_CBC = u"AES_128_CBC"
    

class VMDeleteMode(object):
    """ VMDeleteMode """

    TIMER = u"TIMER"
    

class NSPortPortType(object):
    """ NSPortPortType """

    ACCESS = u"ACCESS"
    NETWORK = u"NETWORK"
    

class GroupRole(object):
    """ GroupRole """

    CSPOPERATOR = u"CSPOPERATOR"
    ORGADMIN = u"ORGADMIN"
    UNKNOWN = u"UNKNOWN"
    CSPROOT = u"CSPROOT"
    SYSTEM = u"SYSTEM"
    ORGAPPDESIGNER = u"ORGAPPDESIGNER"
    ORGNETWORKDESIGNER = u"ORGNETWORKDESIGNER"
    JMS = u"JMS"
    ORGUSER = u"ORGUSER"
    CMS = u"CMS"
    USER = u"USER"
    

class IngressACLEntryTemplateAction(object):
    """ IngressACLEntryTemplateAction """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class JobStatus(object):
    """ JobStatus """

    FAILED = u"FAILED"
    RUNNING = u"RUNNING"
    SUCCESS = u"SUCCESS"
    

class EgressACLEntryTemplateAssociatedApplicationObjectType(object):
    """ EgressACLEntryTemplateAssociatedApplicationObjectType """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class PolicyGroupType(object):
    """ PolicyGroupType """

    HARDWARE = u"HARDWARE"
    SOFTWARE = u"SOFTWARE"
    

class VPortOperationalState(object):
    """ VPortOperationalState """

    DOWN = u"DOWN"
    INIT = u"INIT"
    UP = u"UP"
    

class AutoDiscoveredGatewayPersonality(object):
    """ AutoDiscoveredGatewayPersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class GroupKeyEncryptionProfileSEKPayloadEncryptionAlgorithm(object):
    """ GroupKeyEncryptionProfileSEKPayloadEncryptionAlgorithm """

    RSA_1024 = u"RSA_1024"
    

class IngressAdvFwdEntryTemplateNetworkType(object):
    """ IngressAdvFwdEntryTemplateNetworkType """

    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ENDPOINT_DOMAIN = u"ENDPOINT_DOMAIN"
    ZONE = u"ZONE"
    ENDPOINT_ZONE = u"ENDPOINT_ZONE"
    NETWORK_MACRO_GROUP = u"NETWORK_MACRO_GROUP"
    ENDPOINT_SUBNET = u"ENDPOINT_SUBNET"
    INTERNET_POLICYGROUP = u"INTERNET_POLICYGROUP"
    PUBLIC_NETWORK = u"PUBLIC_NETWORK"
    ENTERPRISE_NETWORK = u"ENTERPRISE_NETWORK"
    ANY = u"ANY"
    

class L2DomainTemplatePolicyChangeStatus(object):
    """ L2DomainTemplatePolicyChangeStatus """

    IPV4 = u"IPV4"
    IPV6 = u"IPV6"
    

class EgressQOSPolicyQueue1ForwardingClasses(object):
    """ EgressQOSPolicyQueue1ForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class VRSClusterNodeRole(object):
    """ VRSClusterNodeRole """

    NONE = u"NONE"
    PRIMARY = u"PRIMARY"
    SECONDARY = u"SECONDARY"
    

class AlarmSeverity(object):
    """ AlarmSeverity """

    INFO = u"INFO"
    CRITICAL = u"CRITICAL"
    MAJOR = u"MAJOR"
    WARNING = u"WARNING"
    MINOR = u"MINOR"
    

class EnterpriseProfileAllowedForwardingClasses(object):
    """ EnterpriseProfileAllowedForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class PortPortType(object):
    """ PortPortType """

    ACCESS = u"ACCESS"
    NETWORK = u"NETWORK"
    

class ExternalServiceServiceType(object):
    """ ExternalServiceServiceType """

    L2 = u"L2"
    L3 = u"L3"
    

class RedundancyGroupRedundantGatewayStatus(object):
    """ RedundancyGroupRedundantGatewayStatus """

    FAILED = u"FAILED"
    SUCCESS = u"SUCCESS"
    

class SystemConfigGroupKeyDefaultSeedPayloadEncryptionAlgorithm(object):
    """ SystemConfigGroupKeyDefaultSeedPayloadEncryptionAlgorithm """

    TRIPLE_DES_CBC = u"TRIPLE_DES_CBC"
    AES_256_CBC = u"AES_256_CBC"
    AES_128_CBC = u"AES_128_CBC"
    

class ExternalAppServiceIngressType(object):
    """ ExternalAppServiceIngressType """

    REDIRECT = u"REDIRECT"
    ROUTE = u"ROUTE"
    

class VPortType(object):
    """ VPortType """

    BRIDGE = u"BRIDGE"
    HOST = u"HOST"
    VM = u"VM"
    

class VSDComponentType(object):
    """ VSDComponentType """

    MEDIATOR = u"MEDIATOR"
    JBOSS = u"JBOSS"
    PERCONA = u"PERCONA"
    EJABBERD = u"EJABBERD"
    STATSSERVER = u"STATSSERVER"
    STATSCOLLECTOR = u"STATSCOLLECTOR"
    TCA = u"TCA"
    

class RedirectionTargetTriggerType(object):
    """ RedirectionTargetTriggerType """

    NONE = u"NONE"
    GARP = u"GARP"
    

class VSDStatus(object):
    """ VSDStatus """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class EgressACLEntryTemplateAction(object):
    """ EgressACLEntryTemplateAction """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class NSRedundantGWGrpRedundantGatewayStatus(object):
    """ NSRedundantGWGrpRedundantGatewayStatus """

    FAILED = u"FAILED"
    SUCCESS = u"SUCCESS"
    

class IPType(object):
    """ IPType """

    IPV4 = u"IPV4"
    IPV6 = u"IPV6"
    

class DomainPATEnabled(object):
    """ DomainPATEnabled """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class SystemConfigGroupKeyDefaultTrafficEncryptionAlgorithm(object):
    """ SystemConfigGroupKeyDefaultTrafficEncryptionAlgorithm """

    AES_192_CBC = u"AES_192_CBC"
    TRIPLE_DES_CBC = u"TRIPLE_DES_CBC"
    AES_256_CBC = u"AES_256_CBC"
    AES_128_CBC = u"AES_128_CBC"
    

class IngressAdvFwdEntryTemplatePolicyState(object):
    """ IngressAdvFwdEntryTemplatePolicyState """

    LIVE = u"LIVE"
    DRAFT = u"DRAFT"
    

class WANServiceConfigType(object):
    """ WANServiceConfigType """

    DYNAMIC = u"DYNAMIC"
    STATIC = u"STATIC"
    

class NSPortTemplatePortType(object):
    """ NSPortTemplatePortType """

    ACCESS = u"ACCESS"
    NETWORK = u"NETWORK"
    

class EnterpriseAvatarType(object):
    """ EnterpriseAvatarType """

    URL = u"URL"
    COMPUTEDURL = u"COMPUTEDURL"
    BASE64 = u"BASE64"
    

class SubnetDefaultAction(object):
    """ SubnetDefaultAction """

    USE_UNDERLAY = u"USE_UNDERLAY"
    DROP_TRAFFIC = u"DROP_TRAFFIC"
    

class GroupKeyEncryptionProfileTrafficAuthenticationAlgorithm(object):
    """ GroupKeyEncryptionProfileTrafficAuthenticationAlgorithm """

    HMAC_MD5 = u"HMAC_MD5"
    HMAC_SHA256 = u"HMAC_SHA256"
    HMAC_SHA1 = u"HMAC_SHA1"
    HMAC_SHA512 = u"HMAC_SHA512"
    HMAC_SHA384 = u"HMAC_SHA384"
    

class VSDComponentStatus(object):
    """ VSDComponentStatus """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class SystemConfigGroupKeyDefaultSeedPayloadAuthenticationAlgorithm(object):
    """ SystemConfigGroupKeyDefaultSeedPayloadAuthenticationAlgorithm """

    HMAC_SHA256 = u"HMAC_SHA256"
    HMAC_SHA1 = u"HMAC_SHA1"
    HMAC_SHA512 = u"HMAC_SHA512"
    

class SystemConfigGroupKeyDefaultSEKPayloadSigningAlgorithm(object):
    """ SystemConfigGroupKeyDefaultSEKPayloadSigningAlgorithm """

    SHA256WITHRSA = u"SHA256WITHRSA"
    SHA384WITHRSA = u"SHA384WITHRSA"
    SHA1WITHRSA = u"SHA1WITHRSA"
    SHA512WITHRSA = u"SHA512WITHRSA"
    SHA224WITHRSA = u"SHA224WITHRSA"
    

class MultiCastListMcastType(object):
    """ MultiCastListMcastType """

    RECEIVE = u"RECEIVE"
    SEND = u"SEND"
    

class IngressAdvFwdEntryTemplateFCOverride(object):
    """ IngressAdvFwdEntryTemplateFCOverride """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class ExternalServiceDirection(object):
    """ ExternalServiceDirection """

    INGRESS = u"INGRESS"
    

class InfrastructurePortProfileSpeed(object):
    """ InfrastructurePortProfileSpeed """

    BASEX10G = u"BASEX10G"
    BASETX100 = u"BASETX100"
    AUTONEGOTIATE = u"AUTONEGOTIATE"
    BASET1000 = u"BASET1000"
    BASET10 = u"BASET10"
    

class IngressAdvFwdEntryTemplateLocationType(object):
    """ IngressAdvFwdEntryTemplateLocationType """

    VPORTTAG = u"VPORTTAG"
    REDIRECTIONTARGET = u"REDIRECTIONTARGET"
    ZONE = u"ZONE"
    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ANY = u"ANY"
    

class VPortSystemType(object):
    """ VPortSystemType """

    NUAGE_VRSG = u"NUAGE_VRSG"
    HARDWARE = u"HARDWARE"
    NUAGE_2 = u"NUAGE_2"
    NUAGE_1 = u"NUAGE_1"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    SOFTWARE = u"SOFTWARE"
    

class IngressExternalServiceTemplateEntryPolicyState(object):
    """ IngressExternalServiceTemplateEntryPolicyState """

    LIVE = u"LIVE"
    DRAFT = u"DRAFT"
    

class EgressQOSPolicyQueue2ForwardingClasses(object):
    """ EgressQOSPolicyQueue2ForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class DomainTemplatePolicyChangeStatus(object):
    """ DomainTemplatePolicyChangeStatus """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    

class VLANStatus(object):
    """ VLANStatus """

    READY = u"READY"
    MISMATCH = u"MISMATCH"
    ORPHAN = u"ORPHAN"
    INITIALIZED = u"INITIALIZED"
    

class KeyServerMonitorSEKSeedPayloadEncryptionAlgorithm(object):
    """ KeyServerMonitorSEKSeedPayloadEncryptionAlgorithm """

    TRIPLE_DES_CBC = u"TRIPLE_DES_CBC"
    AES_256_CBC = u"AES_256_CBC"
    AES_128_CBC = u"AES_128_CBC"
    

class IngressExternalServiceTemplateEntryAssociatedApplicationObjectType(object):
    """ IngressExternalServiceTemplateEntryAssociatedApplicationObjectType """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class DomainTunnelType(object):
    """ DomainTunnelType """

    DC_DEFAULT = u"DC_DEFAULT"
    VXLAN = u"VXLAN"
    GRE = u"GRE"
    

class KeyServerMonitorSeedSeedTrafficAuthenticationAlgorithm(object):
    """ KeyServerMonitorSeedSeedTrafficAuthenticationAlgorithm """

    HMAC_MD5 = u"HMAC_MD5"
    HMAC_SHA256 = u"HMAC_SHA256"
    HMAC_SHA1 = u"HMAC_SHA1"
    HMAC_SHA512 = u"HMAC_SHA512"
    HMAC_SHA384 = u"HMAC_SHA384"
    

class ExternalAppServiceEgressType(object):
    """ ExternalAppServiceEgressType """

    REDIRECT = u"REDIRECT"
    ROUTE = u"ROUTE"
    

class EnterpriseAllowedForwardingClasses(object):
    """ EnterpriseAllowedForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class SystemConfigGroupKeyDefaultSEKPayloadEncryptionAlgorithm(object):
    """ SystemConfigGroupKeyDefaultSEKPayloadEncryptionAlgorithm """

    RSA_1024 = u"RSA_1024"
    

class SystemConfigDomainTunnelType(object):
    """ SystemConfigDomainTunnelType """

    DC_DEFAULT = u"DC_DEFAULT"
    VXLAN = u"VXLAN"
    GRE = u"GRE"
    

class InfrastructureGatewayProfileRemoteLogMode(object):
    """ InfrastructureGatewayProfileRemoteLogMode """

    DISABLED = u"DISABLED"
    SCP = u"SCP"
    RSYSLOG = u"RSYSLOG"
    SFTP = u"SFTP"
    

class NetworkLayoutServiceType(object):
    """ NetworkLayoutServiceType """

    SUBNET_ONLY = u"SUBNET_ONLY"
    ROUTER_ONLY = u"ROUTER_ONLY"
    ROUTER_SWITCH = u"ROUTER_SWITCH"
    

class ApplicationServiceDirection(object):
    """ ApplicationServiceDirection """

    UNIDIRECTIONAL = u"UNIDIRECTIONAL"
    REFLEXIVE = u"REFLEXIVE"
    

class EgressACLEntryTemplateLocationType(object):
    """ EgressACLEntryTemplateLocationType """

    VPORTTAG = u"VPORTTAG"
    REDIRECTIONTARGET = u"REDIRECTIONTARGET"
    ZONE = u"ZONE"
    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ANY = u"ANY"
    

class IngressAdvFwdEntryTemplateAssociatedApplicationObjectType(object):
    """ IngressAdvFwdEntryTemplateAssociatedApplicationObjectType """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class EgressQOSPolicyQueue4ForwardingClasses(object):
    """ EgressQOSPolicyQueue4ForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class BGPPeerStatus(object):
    """ BGPPeerStatus """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class IngressAdvFwdEntryTemplateUplinkPreference(object):
    """ IngressAdvFwdEntryTemplateUplinkPreference """

    SYMMETRIC = u"SYMMETRIC"
    PRIMARY_SECONDARY = u"PRIMARY_SECONDARY"
    SECONDARY_PRIMARY = u"SECONDARY_PRIMARY"
    PRIMARY = u"PRIMARY"
    SECONDARY = u"SECONDARY"
    

class ZoneEncryption(object):
    """ ZoneEncryption """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class GroupKeyEncryptionProfileSeedPayloadEncryptionAlgorithm(object):
    """ GroupKeyEncryptionProfileSeedPayloadEncryptionAlgorithm """

    TRIPLE_DES_CBC = u"TRIPLE_DES_CBC"
    AES_256_CBC = u"AES_256_CBC"
    AES_128_CBC = u"AES_128_CBC"
    

class IngressACLEntryTemplateNetworkType(object):
    """ IngressACLEntryTemplateNetworkType """

    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ENDPOINT_DOMAIN = u"ENDPOINT_DOMAIN"
    ZONE = u"ZONE"
    ENDPOINT_ZONE = u"ENDPOINT_ZONE"
    NETWORK_MACRO_GROUP = u"NETWORK_MACRO_GROUP"
    ENDPOINT_SUBNET = u"ENDPOINT_SUBNET"
    INTERNET_POLICYGROUP = u"INTERNET_POLICYGROUP"
    PUBLIC_NETWORK = u"PUBLIC_NETWORK"
    ENTERPRISE_NETWORK = u"ENTERPRISE_NETWORK"
    ANY = u"ANY"
    

class GatewayTemplatePersonality(object):
    """ GatewayTemplatePersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class VMResyncStatus(object):
    """ VMResyncStatus """

    IN_PROGRESS = u"IN_PROGRESS"
    SUCCESS = u"SUCCESS"
    

class VSCStatus(object):
    """ VSCStatus """

    DOWN = u"DOWN"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class VSDMode(object):
    """ VSDMode """

    CLUSTER = u"CLUSTER"
    STANDALONE = u"STANDALONE"
    

class KeyServerMonitorSEKSeedPayloadAuthenticationAlgorithm(object):
    """ KeyServerMonitorSEKSeedPayloadAuthenticationAlgorithm """

    HMAC_SHA256 = u"HMAC_SHA256"
    HMAC_SHA1 = u"HMAC_SHA1"
    HMAC_SHA512 = u"HMAC_SHA512"
    

class BootstrapStatus(object):
    """ BootstrapStatus """

    NOTIFICATION_APP_REQ_SENT = u"NOTIFICATION_APP_REQ_SENT"
    ACTIVE = u"ACTIVE"
    CERTIFICATE_SIGNED = u"CERTIFICATE_SIGNED"
    INACTIVE = u"INACTIVE"
    NOTIFICATION_APP_REQ_ACK = u"NOTIFICATION_APP_REQ_ACK"
    

class QOSServiceClass(object):
    """ QOSServiceClass """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class IngressACLEntryTemplateLocationType(object):
    """ IngressACLEntryTemplateLocationType """

    VPORTTAG = u"VPORTTAG"
    REDIRECTIONTARGET = u"REDIRECTIONTARGET"
    ZONE = u"ZONE"
    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ANY = u"ANY"
    

class AddressRangeDHCPPoolType(object):
    """ AddressRangeDHCPPoolType """

    BRIDGE = u"BRIDGE"
    HOST = u"HOST"
    

class Multicast(object):
    """ Multicast """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class VPortAddressSpoofing(object):
    """ VPortAddressSpoofing """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class WANServiceServiceType(object):
    """ WANServiceServiceType """

    L2 = u"L2"
    L3 = u"L3"
    

class IngressAdvFwdEntryTemplateAction(object):
    """ IngressAdvFwdEntryTemplateAction """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class NSPortStatus(object):
    """ NSPortStatus """

    READY = u"READY"
    MISMATCH = u"MISMATCH"
    ORPHAN = u"ORPHAN"
    INITIALIZED = u"INITIALIZED"
    

class StatsCollectorInfoAddressType(object):
    """ StatsCollectorInfoAddressType """

    IP = u"IP"
    FQDN = u"FQDN"
    

class RedundancyGroupPersonality(object):
    """ RedundancyGroupPersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class L2DomainUplinkPreference(object):
    """ L2DomainUplinkPreference """

    SYMMETRIC = u"SYMMETRIC"
    PRIMARY_SECONDARY = u"PRIMARY_SECONDARY"
    SECONDARY_PRIMARY = u"SECONDARY_PRIMARY"
    PRIMARY = u"PRIMARY"
    SECONDARY = u"SECONDARY"
    

class GroupKeyEncryptionProfileSeedPayloadAuthenticationAlgorithm(object):
    """ GroupKeyEncryptionProfileSeedPayloadAuthenticationAlgorithm """

    HMAC_SHA256 = u"HMAC_SHA256"
    HMAC_SHA1 = u"HMAC_SHA1"
    HMAC_SHA512 = u"HMAC_SHA512"
    

class PermittedAction(object):
    """ PermittedAction """

    USE = u"USE"
    EXTEND = u"EXTEND"
    DEPLOY = u"DEPLOY"
    READ = u"READ"
    INSTANTIATE = u"INSTANTIATE"
    ALL = u"ALL"
    

class ExternalServiceStage(object):
    """ ExternalServiceStage """

    START = u"START"
    

class IngressExternalServiceTemplateEntryNetworkType(object):
    """ IngressExternalServiceTemplateEntryNetworkType """

    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ENDPOINT_DOMAIN = u"ENDPOINT_DOMAIN"
    ZONE = u"ZONE"
    ENDPOINT_ZONE = u"ENDPOINT_ZONE"
    NETWORK_MACRO_GROUP = u"NETWORK_MACRO_GROUP"
    ENDPOINT_SUBNET = u"ENDPOINT_SUBNET"
    INTERNET_POLICYGROUP = u"INTERNET_POLICYGROUP"
    PUBLIC_NETWORK = u"PUBLIC_NETWORK"
    ENTERPRISE_NETWORK = u"ENTERPRISE_NETWORK"
    ANY = u"ANY"
    
