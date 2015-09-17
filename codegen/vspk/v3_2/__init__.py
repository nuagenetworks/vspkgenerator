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


from .nuvsp import NUVSP
from .nul2domain import NUL2Domain
from .nuautodiscoveredgateway import NUAutoDiscoveredGateway
from .nuport import NUPort
from .nuuplinkrd import NUUplinkRD
from .nudscpforwardingclassmapping import NUDSCPForwardingClassMapping
from .nuvcentercluster import NUVCenterCluster
from .nulicense import NULicense
from .nuqos import NUQOS
from .nuingressacltemplate import NUIngressACLTemplate
from .nuexternalappservice import NUExternalAppService
from .nubgppeer import NUBGPPeer
from .nugroup import NUGroup
from .nuapplicationservice import NUApplicationService
from .nuhostinterface import NUHostInterface
from .nulocation import NULocation
from .nuvcenterdatacenter import NUVCenterDataCenter
from .nuendpoint import NUEndPoint
from .nuvcentervrsconfig import NUVCenterVRSConfig
from .nuegressqospolicy import NUEgressQOSPolicy
from .nuenterprisepermission import NUEnterprisePermission
from .nusystemconfig import NUSystemConfig
from .nurestuser import NURESTUser
from .nustatscollectorinfo import NUStatsCollectorInfo
from .nuinfrastructureconfig import NUInfrastructureConfig
from .nubridgeinterface import NUBridgeInterface
from .nuratelimiter import NURateLimiter
from .nueventlog import NUEventLog
from .nukeyservermonitorseed import NUKeyServerMonitorSeed
from .nuaddressrange import NUAddressRange
from .numonitoringport import NUMonitoringPort
from .nuvlan import NUVLAN
from .nuenterprise import NUEnterprise
from .nuredirectiontargettemplate import NURedirectionTargetTemplate
from .nusharednetworkresource import NUSharedNetworkResource
from .nuvsd import NUVSD
from .nuvpnconnection import NUVPNConnection
from .nuapp import NUApp
from .nuflowforwardingpolicy import NUFlowForwardingPolicy
from .nuinfrastructurevscprofile import NUInfrastructureVscProfile
from .nuvcenter import NUVCenter
from .nutca import NUTCA
from .nuvcenterhypervisor import NUVCenterHypervisor
from .nukeyservermonitorencryptedsek import NUKeyServerMonitorEncryptedSEK
from .nuporttemplate import NUPortTemplate
from .nuvrs import NUVRS
from .numulticastrange import NUMultiCastRange
from .nuipreservation import NUIPReservation
from .nustatistics import NUStatistics
from .nunsport import NUNSPort
from .nunsportstaticconfiguration import NUNSPortStaticConfiguration
from .nucloudmgmtsystem import NUCloudMgmtSystem
from .nudomaintemplate import NUDomainTemplate
from .nuvirtualip import NUVirtualIP
from .nuvminterface import NUVMInterface
from .nuinfrastructureportprofile import NUInfrastructurePortProfile
from .nukeyservermonitor import NUKeyServerMonitor
from .nupermittedaction import NUPermittedAction
from .numetadatatag import NUMetadataTag
from .nuingressadvfwdentrytemplate import NUIngressAdvFwdEntryTemplate
from .nuzone import NUZone
from .nuegressacltemplate import NUEgressACLTemplate
from .nuldapconfiguration import NULDAPConfiguration
from .nutier import NUTier
from .nuingressaclentrytemplate import NUIngressACLEntryTemplate
from .nugatewaytemplate import NUGatewayTemplate
from .nubootstrap import NUBootstrap
from .nusiteinfo import NUSiteInfo
from .nuredirectiontarget import NURedirectionTarget
from .nuenterpriseprofile import NUEnterpriseProfile
from .nucertificate import NUCertificate
from .nupolicygroup import NUPolicyGroup
from .nukeyservermonitorsek import NUKeyServerMonitorSEK
from .nuhsc import NUHSC
from .nuvm import NUVM
from .numulticastchannelmap import NUMultiCastChannelMap
from .nuvcentereamconfig import NUVCenterEAMConfig
from .nuvport import NUVPort
from .numulticastlist import NUMultiCastList
from .nunsgatewaytemplate import NUNSGatewayTemplate
from .nuaggregatemetadata import NUAggregateMetadata
from .numirrordestination import NUMirrorDestination
from .nuwanservice import NUWANService
from .nupolicydecision import NUPolicyDecision
from .nuexternalservice import NUExternalService
from .nuzonetemplate import NUZoneTemplate
from .nunatmapentry import NUNATMapEntry
from .nustaticroute import NUStaticRoute
from .nuvlantemplate import NUVLANTemplate
from .nuredundancygroup import NURedundancyGroup
from .nuglobalmetadata import NUGlobalMetadata
from .nuvmresync import NUVMResync
from .nudscpforwardingclasstable import NUDSCPForwardingClassTable
from .nuingressexternalservicetemplate import NUIngressExternalServiceTemplate
from .nuenterprisenetwork import NUEnterpriseNetwork
from .nuvportmirror import NUVPortMirror
from .nualarm import NUAlarm
from .nukeyservermonitorencryptedseed import NUKeyServerMonitorEncryptedSeed
from .nuinfrastructuregatewayprofile import NUInfrastructureGatewayProfile
from .nugroupkeyencryptionprofile import NUGroupKeyEncryptionProfile
from .nupublicnetworkmacro import NUPublicNetworkMacro
from .nunsporttemplate import NUNSPortTemplate
from .nupolicygrouptemplate import NUPolicyGroupTemplate
from .numultinicvport import NUMultiNICVPort
from .nuflowsecuritypolicy import NUFlowSecurityPolicy
from .nuvcentervrsaddressrange import NUVCenterVRSAddressRange
from .nuflow import NUFlow
from .nusubnettemplate import NUSubnetTemplate
from .nuredundantport import NURedundantPort
from .numetadata import NUMetadata
from .nuuser import NUUser
from .nuvsc import NUVSC
from .nuegressaclentrytemplate import NUEgressACLEntryTemplate
from .nunetworklayout import NUNetworkLayout
from .nuvsdcomponent import NUVSDComponent
from .nusubnet import NUSubnet
from .nuingressadvfwdtemplate import NUIngressAdvFwdTemplate
from .nufloatingip import NUFloatingIp
from .nunetworkmacrogroup import NUNetworkMacroGroup
from .nupatnatpool import NUPATNATPool
from .nuingressexternalservicetemplateentry import NUIngressExternalServiceTemplateEntry
from .nugateway import NUGateway
from .nunsgateway import NUNSGateway
from .nustatisticspolicy import NUStatisticsPolicy
from .nujob import NUJob
from .nudhcpoption import NUDHCPOption
from .nubootstrapactivation import NUBootstrapActivation
from .nunsredundantgwgrp import NUNSRedundantGWGrp
from .nul2domaintemplate import NUL2DomainTemplate
from .nudomain import NUDomain
from .nuvsdsession import NUVSDSession

__all__ = ["NUVSP", "NUL2Domain", "NUAutoDiscoveredGateway", "NUPort", "NUUplinkRD", "NUDSCPForwardingClassMapping", "NUVCenterCluster", "NULicense", "NUQOS", "NUIngressACLTemplate", "NUExternalAppService", "NUBGPPeer", "NUGroup", "NUApplicationService", "NUHostInterface", "NULocation", "NUVCenterDataCenter", "NUEndPoint", "NUVCenterVRSConfig", "NUEgressQOSPolicy", "NUEnterprisePermission", "NUSystemConfig", "NURESTUser", "NUStatsCollectorInfo", "NUInfrastructureConfig", "NUBridgeInterface", "NURateLimiter", "NUEventLog", "NUKeyServerMonitorSeed", "NUAddressRange", "NUMonitoringPort", "NUVLAN", "NUEnterprise", "NURedirectionTargetTemplate", "NUSharedNetworkResource", "NUVSD", "NUVPNConnection", "NUApp", "NUFlowForwardingPolicy", "NUInfrastructureVscProfile", "NUVCenter", "NUTCA", "NUVCenterHypervisor", "NUKeyServerMonitorEncryptedSEK", "NUPortTemplate", "NUVRS", "NUMultiCastRange", "NUIPReservation", "NUStatistics", "NUNSPort", "NUNSPortStaticConfiguration", "NUCloudMgmtSystem", "NUDomainTemplate", "NUVirtualIP", "NUVMInterface", "NUInfrastructurePortProfile", "NUKeyServerMonitor", "NUPermittedAction", "NUMetadataTag", "NUIngressAdvFwdEntryTemplate", "NUZone", "NUEgressACLTemplate", "NULDAPConfiguration", "NUTier", "NUIngressACLEntryTemplate", "NUGatewayTemplate", "NUBootstrap", "NUSiteInfo", "NURedirectionTarget", "NUEnterpriseProfile", "NUCertificate", "NUPolicyGroup", "NUKeyServerMonitorSEK", "NUHSC", "NUVM", "NUMultiCastChannelMap", "NUVCenterEAMConfig", "NUVPort", "NUMultiCastList", "NUNSGatewayTemplate", "NUAggregateMetadata", "NUMirrorDestination", "NUWANService", "NUPolicyDecision", "NUExternalService", "NUZoneTemplate", "NUNATMapEntry", "NUStaticRoute", "NUVLANTemplate", "NURedundancyGroup", "NUGlobalMetadata", "NUVMResync", "NUDSCPForwardingClassTable", "NUIngressExternalServiceTemplate", "NUEnterpriseNetwork", "NUVPortMirror", "NUAlarm", "NUKeyServerMonitorEncryptedSeed", "NUInfrastructureGatewayProfile", "NUGroupKeyEncryptionProfile", "NUPublicNetworkMacro", "NUNSPortTemplate", "NUPolicyGroupTemplate", "NUMultiNICVPort", "NUFlowSecurityPolicy", "NUVCenterVRSAddressRange", "NUFlow", "NUSubnetTemplate", "NURedundantPort", "NUMetadata", "NUUser", "NUVSC", "NUEgressACLEntryTemplate", "NUNetworkLayout", "NUVSDComponent", "NUSubnet", "NUIngressAdvFwdTemplate", "NUFloatingIp", "NUNetworkMacroGroup", "NUPATNATPool", "NUIngressExternalServiceTemplateEntry", "NUGateway", "NUNSGateway", "NUStatisticsPolicy", "NUJob", "NUDHCPOption", "NUBootstrapActivation", "NUNSRedundantGWGrp", "NUL2DomainTemplate", "NUDomain", 'NUVSDSession']

import pkg_resources
from bambou import BambouConfig, NURESTModelController

default_attrs = pkg_resources.resource_filename(__name__, '/resources/attrs_defaults.ini')
BambouConfig.set_default_values_config_file(default_attrs)

NURESTModelController.register_model(NUVSP)
NURESTModelController.register_model(NUL2Domain)
NURESTModelController.register_model(NUAutoDiscoveredGateway)
NURESTModelController.register_model(NUPort)
NURESTModelController.register_model(NUUplinkRD)
NURESTModelController.register_model(NUDSCPForwardingClassMapping)
NURESTModelController.register_model(NUVCenterCluster)
NURESTModelController.register_model(NULicense)
NURESTModelController.register_model(NUQOS)
NURESTModelController.register_model(NUIngressACLTemplate)
NURESTModelController.register_model(NUExternalAppService)
NURESTModelController.register_model(NUBGPPeer)
NURESTModelController.register_model(NUGroup)
NURESTModelController.register_model(NUApplicationService)
NURESTModelController.register_model(NUHostInterface)
NURESTModelController.register_model(NULocation)
NURESTModelController.register_model(NUVCenterDataCenter)
NURESTModelController.register_model(NUEndPoint)
NURESTModelController.register_model(NUVCenterVRSConfig)
NURESTModelController.register_model(NUEgressQOSPolicy)
NURESTModelController.register_model(NUEnterprisePermission)
NURESTModelController.register_model(NUSystemConfig)
NURESTModelController.register_model(NURESTUser)
NURESTModelController.register_model(NUStatsCollectorInfo)
NURESTModelController.register_model(NUInfrastructureConfig)
NURESTModelController.register_model(NUBridgeInterface)
NURESTModelController.register_model(NURateLimiter)
NURESTModelController.register_model(NUEventLog)
NURESTModelController.register_model(NUKeyServerMonitorSeed)
NURESTModelController.register_model(NUAddressRange)
NURESTModelController.register_model(NUMonitoringPort)
NURESTModelController.register_model(NUVLAN)
NURESTModelController.register_model(NUEnterprise)
NURESTModelController.register_model(NURedirectionTargetTemplate)
NURESTModelController.register_model(NUSharedNetworkResource)
NURESTModelController.register_model(NUVSD)
NURESTModelController.register_model(NUVPNConnection)
NURESTModelController.register_model(NUApp)
NURESTModelController.register_model(NUFlowForwardingPolicy)
NURESTModelController.register_model(NUInfrastructureVscProfile)
NURESTModelController.register_model(NUVCenter)
NURESTModelController.register_model(NUTCA)
NURESTModelController.register_model(NUVCenterHypervisor)
NURESTModelController.register_model(NUKeyServerMonitorEncryptedSEK)
NURESTModelController.register_model(NUPortTemplate)
NURESTModelController.register_model(NUVRS)
NURESTModelController.register_model(NUMultiCastRange)
NURESTModelController.register_model(NUIPReservation)
NURESTModelController.register_model(NUStatistics)
NURESTModelController.register_model(NUNSPort)
NURESTModelController.register_model(NUNSPortStaticConfiguration)
NURESTModelController.register_model(NUCloudMgmtSystem)
NURESTModelController.register_model(NUDomainTemplate)
NURESTModelController.register_model(NUVirtualIP)
NURESTModelController.register_model(NUVMInterface)
NURESTModelController.register_model(NUInfrastructurePortProfile)
NURESTModelController.register_model(NUKeyServerMonitor)
NURESTModelController.register_model(NUPermittedAction)
NURESTModelController.register_model(NUMetadataTag)
NURESTModelController.register_model(NUIngressAdvFwdEntryTemplate)
NURESTModelController.register_model(NUZone)
NURESTModelController.register_model(NUEgressACLTemplate)
NURESTModelController.register_model(NULDAPConfiguration)
NURESTModelController.register_model(NUTier)
NURESTModelController.register_model(NUIngressACLEntryTemplate)
NURESTModelController.register_model(NUGatewayTemplate)
NURESTModelController.register_model(NUBootstrap)
NURESTModelController.register_model(NUSiteInfo)
NURESTModelController.register_model(NURedirectionTarget)
NURESTModelController.register_model(NUEnterpriseProfile)
NURESTModelController.register_model(NUCertificate)
NURESTModelController.register_model(NUPolicyGroup)
NURESTModelController.register_model(NUKeyServerMonitorSEK)
NURESTModelController.register_model(NUHSC)
NURESTModelController.register_model(NUVM)
NURESTModelController.register_model(NUMultiCastChannelMap)
NURESTModelController.register_model(NUVCenterEAMConfig)
NURESTModelController.register_model(NUVPort)
NURESTModelController.register_model(NUMultiCastList)
NURESTModelController.register_model(NUNSGatewayTemplate)
NURESTModelController.register_model(NUAggregateMetadata)
NURESTModelController.register_model(NUMirrorDestination)
NURESTModelController.register_model(NUWANService)
NURESTModelController.register_model(NUPolicyDecision)
NURESTModelController.register_model(NUExternalService)
NURESTModelController.register_model(NUZoneTemplate)
NURESTModelController.register_model(NUNATMapEntry)
NURESTModelController.register_model(NUStaticRoute)
NURESTModelController.register_model(NUVLANTemplate)
NURESTModelController.register_model(NURedundancyGroup)
NURESTModelController.register_model(NUGlobalMetadata)
NURESTModelController.register_model(NUVMResync)
NURESTModelController.register_model(NUDSCPForwardingClassTable)
NURESTModelController.register_model(NUIngressExternalServiceTemplate)
NURESTModelController.register_model(NUEnterpriseNetwork)
NURESTModelController.register_model(NUVPortMirror)
NURESTModelController.register_model(NUAlarm)
NURESTModelController.register_model(NUKeyServerMonitorEncryptedSeed)
NURESTModelController.register_model(NUInfrastructureGatewayProfile)
NURESTModelController.register_model(NUGroupKeyEncryptionProfile)
NURESTModelController.register_model(NUPublicNetworkMacro)
NURESTModelController.register_model(NUNSPortTemplate)
NURESTModelController.register_model(NUPolicyGroupTemplate)
NURESTModelController.register_model(NUMultiNICVPort)
NURESTModelController.register_model(NUFlowSecurityPolicy)
NURESTModelController.register_model(NUVCenterVRSAddressRange)
NURESTModelController.register_model(NUFlow)
NURESTModelController.register_model(NUSubnetTemplate)
NURESTModelController.register_model(NURedundantPort)
NURESTModelController.register_model(NUMetadata)
NURESTModelController.register_model(NUUser)
NURESTModelController.register_model(NUVSC)
NURESTModelController.register_model(NUEgressACLEntryTemplate)
NURESTModelController.register_model(NUNetworkLayout)
NURESTModelController.register_model(NUVSDComponent)
NURESTModelController.register_model(NUSubnet)
NURESTModelController.register_model(NUIngressAdvFwdTemplate)
NURESTModelController.register_model(NUFloatingIp)
NURESTModelController.register_model(NUNetworkMacroGroup)
NURESTModelController.register_model(NUPATNATPool)
NURESTModelController.register_model(NUIngressExternalServiceTemplateEntry)
NURESTModelController.register_model(NUGateway)
NURESTModelController.register_model(NUNSGateway)
NURESTModelController.register_model(NUStatisticsPolicy)
NURESTModelController.register_model(NUJob)
NURESTModelController.register_model(NUDHCPOption)
NURESTModelController.register_model(NUBootstrapActivation)
NURESTModelController.register_model(NUNSRedundantGWGrp)
NURESTModelController.register_model(NUL2DomainTemplate)
NURESTModelController.register_model(NUDomain)
