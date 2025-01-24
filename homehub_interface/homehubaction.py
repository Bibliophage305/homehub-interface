from abc import ABC


class HomeHubActionBase(ABC):
    def as_dict(self):
        ret = {}
        for k, v in sorted(self.__dict__.items(), key=lambda x: x[0]):
            if v is None:
                continue
            elif isinstance(v, HomeHubActionBase):
                ret[k] = v.as_dict()
            else:
                ret[k] = v
        return ret

    def __str__(self):
        return str(self.as_dict())


class HomeHubActionOptionsCapabilityFlags(HomeHubActionBase):
    def __init__(self, interface: bool = None):
        self.interface = interface


class HomeHubActionOptions(HomeHubActionBase):
    def __init__(self, capability_flags: HomeHubActionOptionsCapabilityFlags = None):
        self.capability_flags = capability_flags


class HomeHubAction(HomeHubActionBase, ABC):
    admin_required = False

    def set_id(self, id: int):
        self.id = id


class HomeHubActionATMLinksLinkAliasATM_DATADestinationAddressGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/ATM/Links/Link[Alias='ATM_DATA']/DestinationAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionATMLinksLinkAliasATM_TVDestinationAddressGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/ATM/Links/Link[Alias='ATM_TV']/DestinationAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasDEFAULT_POOLEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='DEFAULT_POOL']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasDEFAULT_POOLIPInterfaceGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='DEFAULT_POOL']/IPInterface"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasDEFAULT_POOLLeaseTimeGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='DEFAULT_POOL']/LeaseTime"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasDEFAULT_POOLMaxAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='DEFAULT_POOL']/MaxAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasDEFAULT_POOLMinAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='DEFAULT_POOL']/MinAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasDEFAULT_POOLStaticAddressesGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/DHCPv4/Server/Pools/Pool[Alias='DEFAULT_POOL']/StaticAddresses"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDHCPv4ServerPoolsPoolAliasDEFAULT_POOLSubnetMaskGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='DEFAULT_POOL']/SubnetMask"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDHCPv4ServerPoolsPoolAliasOPENWIFI_POOLIPInterfaceGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/DHCPv4/Server/Pools/Pool[Alias='OPENWIFI_POOL']/IPInterface"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasOPENWIFI_POOLMaxAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='OPENWIFI_POOL']/MaxAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasOPENWIFI_POOLMinAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='OPENWIFI_POOL']/MinAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv4ServerPoolsPoolAliasOPENWIFI_POOLSubnetMaskGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/Pools/Pool[Alias='OPENWIFI_POOL']/SubnetMask"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDHCPv4ServerX_SAGEMCOM_AuthoritativeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv4/Server/X_SAGEMCOM_Authoritative"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv6ServerPoolsPoolAliasDEFAULT_POOLClientsClientActivetrueIPv6AddressesIPv6AddressIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv6/Server/Pools/Pool[Alias='DEFAULT_POOL']/Clients/Client[Active='true']/IPv6Addresses/IPv6Address/IPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDHCPv6ServerPoolsPoolAliasDEFAULT_POOLIANAEnableGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv6/Server/Pools/Pool[Alias='DEFAULT_POOL']/IANAEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDHCPv6ServerPoolsPoolAliasDEFAULT_POOLStatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DHCPv6/Server/Pools/Pool[Alias='DEFAULT_POOL']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDNSClientHostNameGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DNS/Client/HostName"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDNSClientLocalDomainsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DNS/Client/LocalDomains"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDNSRelayForwardingsForwardingStatusENABLEDDNSServerGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/DNS/Relay/Forwardings/Forwarding[Status='ENABLED']/DNSServer"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDNSRelayLocalDomainsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DNS/Relay/LocalDomains"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLChannelsChanneluid1DownstreamCurrRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Channels/Channel[@uid='1']/DownstreamCurrRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLChannelsChanneluid1UpstreamCurrRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Channels/Channel[@uid='1']/UpstreamCurrRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLChannelsChannelAliasDSL0ActualInterleavingDelayGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Channels/Channel[Alias='DSL0']/ActualInterleavingDelay"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDSLChannelsChannelAliasDSL0ActualInterleavingDelayusGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/DSL/Channels/Channel[Alias='DSL0']/ActualInterleavingDelayus"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLChannelsChannelAliasDSL0DownstreamCurrRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Channels/Channel[Alias='DSL0']/DownstreamCurrRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLChannelsChannelAliasDSL0UpstreamCurrRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Channels/Channel[Alias='DSL0']/UpstreamCurrRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLLinesLineuid1LastChangeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[@uid='1']/LastChange"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLLinesLineuid1StatsBytesReceivedGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[@uid='1']/Stats/BytesReceived"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDSLLinesLineuid1StatsBytesSentGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[@uid='1']/Stats/BytesSent"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDSLLinesLineAliasDSL0DownstreamAttenuationGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/DownstreamAttenuation"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDSLLinesLineAliasDSL0DownstreamMaxBitRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/DownstreamMaxBitRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLLinesLineAliasDSL0DownstreamNoiseMarginGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/DownstreamNoiseMargin"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDSLLinesLineAliasDSL0FirmwareVersionGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/FirmwareVersion"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLLinesLineAliasDSL0LastChangeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/LastChange"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLLinesLineAliasDSL0SignalDownstreamAttenuationGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/SignalDownstreamAttenuation"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDSLLinesLineAliasDSL0SignalUpstreamAttenuationGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/SignalUpstreamAttenuation"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDSLLinesLineAliasDSL0StandardUsedGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/StandardUsed"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLLinesLineAliasDSL0StatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLLinesLineAliasDSL0UpstreamAttenuationGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/UpstreamAttenuation"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDSLLinesLineAliasDSL0UpstreamMaxBitRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/UpstreamMaxBitRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDSLLinesLineAliasDSL0UpstreamNoiseMarginGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DSL/Lines/Line[Alias='DSL0']/UpstreamNoiseMargin"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDeviceDiscoveryDeviceIdentificationDeviceTypesGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceDiscovery/DeviceIdentification/DeviceTypes"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoBootloaderVersionGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/BootloaderVersion"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDeviceInfoExternalFirmwareVersionGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/ExternalFirmwareVersion"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoHardwareVersionGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/HardwareVersion"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoMACAddressGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/MACAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoModelNameGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/ModelName"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoProductClassGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/ProductClass"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoProductVariantGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/ProductVariant"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoSerialNumberGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/SerialNumber"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoSupportedDataModelsSupportedDataModelURLGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/SupportedDataModels/SupportedDataModel/URL"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionDeviceInfoUpTimeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/DeviceInfo/UpTime"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionDeviceInfoVendorLogFilesVendorLogFileuid1GetVendorLogDownloadURI(
    HomeHubAction
):
    def __init__(self):
        self.method = "getVendorLogDownloadURI"
        self.xpath = "Device/DeviceInfo/VendorLogFiles/VendorLogFile[@uid='1']"
        self.parameters = {"FileName": "eventLog"}
        self.admin_required = True


class HomeHubActionEthernetInterfacesInterfaceAliasPHY4StatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Ethernet/Interfaces/Interface[Alias='PHY4']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionEthernetInterfacesInterfaceAliasPHY6_WANStatusGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Ethernet/Interfaces/Interface[Alias='PHY6_WAN']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionEthernetInterfacesInterfaceAliasPHY1MACAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Ethernet/Interfaces/Interface[Alias='PHY1']/MACAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionEthernetLinksLinkAliasFTTH_DATALowerLayersGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Ethernet/Links/Link[Alias='FTTH_DATA']/LowerLayers"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionEthernetVLANTerminationsVLANTerminationAliasVLAN_DATAVLANIDGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/Ethernet/VLANTerminations/VLANTermination[Alias='VLAN_DATA']/VLANID"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionFASTLinesLineuid1StatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/FAST/Lines/Line[@uid='1']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionFirewallChainsChainNameCustomRulesGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Firewall/Chains/Chain[Name='Custom']/Rules"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionFirewallChainsChainNameLowRulesRuleIPVersion6GetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/Firewall/Chains/Chain[Name='Low']/Rules/Rule[IPVersion='6']"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionFirewallConfigGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Firewall/Config"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionFirewallEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Firewall/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionFirewallLevelsLevelNameCustomDefaultPolicyGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Firewall/Levels/Level[Name='Custom']/DefaultPolicy"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionFirewallRespondToPingGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Firewall/RespondToPing"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHostsHistoryMaxAgeInDaysGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Hosts/HistoryMaxAgeInDays"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHostsHostsHostBlacklistedScheduleGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Hosts/Hosts/Host/BlacklistedSchedule"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHostsHostsHostuid1GetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Hosts/Hosts/Host[@uid='1']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHostsHostsHostuid4GetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Hosts/Hosts/Host[@uid='4']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHostsHostsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Hosts/Hosts"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPIPv6StatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/IPv6Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_LANIPv6AddressesIPv6AddressIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_LAN']/IPv6Addresses/IPv6Address/IPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_LANIPv6AddressesIPv6AddressAliasLINK_LOCALIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_LAN']/IPv6Addresses/IPv6Address[Alias='LINK_LOCAL']/IPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_LANIPv6AddressesIPv6AddressAliasULA_LANIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_LAN']/IPv6Addresses/IPv6Address[Alias='ULA_LAN']/IPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_LANIPv6AddressesIPv6AddressIPAddressStatusPREFERREDGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_LAN']/IPv6Addresses/IPv6Address[IPAddressStatus='PREFERRED']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_LANIPv6PrefixesIPv6PrefixAliasULA_LANPrefixGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_LAN']/IPv6Prefixes/IPv6Prefix[Alias='ULA_LAN']/Prefix"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_LANIPv6PrefixesGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_LAN']/IPv6Prefixes"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_LANULAEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_LAN']/ULAEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_OPENWIFIIPv4AddressesIPv4AddressAliasIP_BR_OPENWIFI_ADDRESSIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_OPENWIFI']/IPv4Addresses/IPv4Address[Alias='IP_BR_OPENWIFI_ADDRESS']/IPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_BR_OPENWIFIIPv4AddressesIPv4AddressAliasIP_BR_OPENWIFI_ADDRESSSubnetMaskGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_BR_OPENWIFI']/IPv4Addresses/IPv4Address[Alias='IP_BR_OPENWIFI_ADDRESS']/SubnetMask"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAIPv4AddressesIPv4AddressIPGatewayGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/IPv4Addresses/IPv4Address/IPGateway"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAIPv4AddressesIPv4AddressAliasIP_DATA_ADDRESSDnsGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/IPv4Addresses/IPv4Address[Alias='IP_DATA_ADDRESS']/Dns"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAIPv4AddressesIPv4AddressAliasIP_DATA_ADDRESSIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/IPv4Addresses/IPv4Address[Alias='IP_DATA_ADDRESS']/IPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAIPv6AddressesIPv6AddressAliasLINK_LOCALIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/IPv6Addresses/IPv6Address[Alias='LINK_LOCAL']/IPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAIPv6AddressesIPv6AddressIPAddressStatusPREFERREDGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/IPv6Addresses/IPv6Address[IPAddressStatus='PREFERRED']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAIPv6PrefixesGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/IPv6Prefixes"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionIPInterfacesInterfaceAliasIP_DATALastChangeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/LastChange"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAStatsBytesReceivedGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/IP/Interfaces/Interface[Alias='IP_DATA']/Stats/BytesReceived"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAStatsBytesSentGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/Stats/BytesSent"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAIPv4AddressesIPv4AddressAliasIP_DATA_ADDRESSSubnetMaskGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/IPv4Addresses/IPv4Address[Alias='IP_DATA_ADDRESS']/SubnetMask"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAStatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfacesInterfaceAliasIP_DATAStatusSubscribeForNotification(
    HomeHubAction
):
    def __init__(self, id):
        self.method = "subscribeForNotification"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/Status"
        self.parameters = {"id": id, "type": "value-change", "current-value": False}


class HomeHubActionManagementServerTR69InternalDataSettingsPortGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/ManagementServer/TR69InternalData/Settings/Port"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionManagersHubLightControlBrightnessGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/Brightness"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionManagersHubLightControlFrontLEDColorGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/FrontLEDColor"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionManagersHubLightControlLedEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/LedEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionManagersHubLightControlScheduleEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/Schedule/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionManagersHubLightControlScheduleTurnLightOffGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOff"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionManagersHubLightControlScheduleTurnLightOnGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOn"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionManagersNetworkDataDhcpLanMaxAddressGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/NetworkData/DhcpLanMaxAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionManagersNetworkDataDhcpLanMinAddressGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/NetworkData/DhcpLanMinAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionManagersNetworkDataIPv6ModeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/NetworkData/IPv6Mode"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionManagersNetworkDataIpLanGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/NetworkData/IpLan"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionManagersNetworkDataNetmaskLanGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/NetworkData/NetmaskLan"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionManagersNetworkDataObfuscatedPPPPasswordGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/NetworkData/ObfuscatedPPPPassword"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionNATPortMappingsPortMappingAliasAPI_DMZInternalClientGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/NAT/PortMappings/PortMapping[Alias='API_DMZ']/InternalClient"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionNATPortMappingsPortMappingAliasAPI_DMZInternalMACAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/NAT/PortMappings/PortMapping[Alias='API_DMZ']/InternalMACAddress"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionNATPortMappingsPortMappingServiceDMZEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/NAT/PortMappings/PortMapping[Service='DMZ']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionNATPortMappingsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/NAT/PortMappings"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionNATSIPALGEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/NAT/SIPALGEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionPPPInterfacesInterfaceAliasPPP_DSL_DATAConnectionStatusGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/ConnectionStatus"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfacesInterfaceAliasPPP_DSL_DATAIPCPLocalIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/IPCP/LocalIPAddress"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionPPPInterfacesInterfaceAliasPPP_DSL_DATAIPCPRemoteIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/IPCP/RemoteIPAddress"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionPPPInterfacesInterfaceAliasPPP_DSL_DATAIPv6CPRemoteInterfaceIdentifierGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/IPv6CP/RemoteInterfaceIdentifier"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionPPPInterfacesInterfaceAliasPPP_DSL_DATAStatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfacesInterfaceAliasPPP_FTTH_DATAConnectionStatusGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/ConnectionStatus"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfacesInterfaceAliasPPP_FTTH_DATAIPCPLocalIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/IPCP/LocalIPAddress"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionPPPInterfacesInterfaceAliasPPP_FTTH_DATAIPCPRemoteIPAddressGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/IPCP/RemoteIPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionPPPInterfacesInterfaceAliasPPP_FTTH_DATAIPv6CPRemoteInterfaceIdentifierGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/IPv6CP/RemoteInterfaceIdentifier"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionPPPInterfacesInterfaceAliasPPP_FTTH_DATAStatusGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfacesInterfaceAliasPPP_DSL_DATAEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfacesInterfaceAliasPPP_DSL_DATAStatusSubscribeForNotification(
    HomeHubAction
):
    def __init__(self, id):
        self.method = "subscribeForNotification"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/Status"
        self.parameters = {"id": id, "type": "value-change", "current-value": False}


class HomeHubActionPPPInterfacesInterfaceAliasPPP_DSL_DATAUsernameGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/Username"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfacesInterfaceAliasPPP_FTTH_DATAEnableGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfacesInterfaceAliasPPP_FTTH_DATAStatusSubscribeForNotification(
    HomeHubAction
):
    def __init__(self, id):
        self.method = "subscribeForNotification"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/Status"
        self.parameters = {"id": id, "type": "value-change", "current-value": False}


class HomeHubActionPPPInterfacesInterfaceAliasPPP_FTTH_DATAUsernameGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/Username"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionRouterAdvertisementInterfaceSettingsInterfaceSettingAliasRA_BR_LANAdvManagedFlagGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/RouterAdvertisement/InterfaceSettings/InterfaceSetting[Alias='RA_BR_LAN']/AdvManagedFlag"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionRouterAdvertisementInterfaceSettingsInterfaceSettingAliasRA_BR_LANAdvOtherConfigFlagGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/RouterAdvertisement/InterfaceSettings/InterfaceSetting[Alias='RA_BR_LAN']/AdvOtherConfigFlag"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionServicesBandwidthMonitoringUploadBMStatisticsFile(HomeHubAction):
    def __init__(self):
        self.method = "uploadBMStatisticsFile"
        self.xpath = "Device/Services/BandwidthMonitoring"
        self.parameters = {"startDate": "20000101", "endDate": "20250122"}


class HomeHubActionServicesBusinessDNSOverrideServersGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/Business/DNSOverrideServers"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesBusinessDNSOverrideGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/Business/DNSOverride"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesBusinessStaticIPAddressAssignationsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/Business/staticIP/AddressAssignations"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesBusinessStaticIPRoutedLANEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/Business/staticIP/RoutedLANEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesDeviceConfigConnectionHURLPageEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/ConnectionHURLPageEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesDeviceConfigDomainLockListGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/DomainLockList"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionServicesDeviceConfigDomainLockingEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/DomainLockingEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesDeviceConfigEnableBridgedModeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/EnableBridgedMode"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesDeviceConfigLastFirmwareUpgradeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/LastFirmwareUpgrade"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionServicesDeviceConfigLastSuccesfulWanTypeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/LastSuccesfulWanType"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesDeviceConfigPortClampingEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/PortClampingEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionServicesDeviceConfigWiFiModeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/WiFiMode"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesDeviceConfigWifiPasswordForbiddenWordsGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/WifiPasswordForbiddenWords"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionServicesDynamicDNSClientsClientuid1GetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DynamicDNS/Clients/Client[@uid='1']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionServicesDynamicDNSServicesGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DynamicDNS/Services"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionServicesOnlineInstallDHCPFingerprintDatabaseEntriesGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/OnlineInstall/DHCPFingerprintDatabase/Entries"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesOnlineInstallEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/OnlineInstall/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesOpenWiFiOpenWifiOptedInGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/OpenWiFi/OpenWifiOptedIn"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesOpenWiFiUIEnabledGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/OpenWiFi/UIEnabled"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesParentalControlGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/ParentalControl"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesStorageServicesStorageServiceuid1LogicalVolumesGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/Services/StorageServices/StorageService[@uid='1']/LogicalVolumes"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesVoiceServicesVoiceServiceAliasVOICESERVICE1CallControlLinesLineAliasLINE1GetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/VoiceServices/VoiceService[Alias='VOICESERVICE1']/CallControl/Lines/Line[Alias='LINE1']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesVoiceServicesVoiceServiceAliasVOICESERVICE1CallLogsGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/Services/VoiceServices/VoiceService[Alias='VOICESERVICE1']/CallLogs"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesVoiceServicesVoiceServiceAliasVOICESERVICE1SIPClientsClientAliasCLIENT1LastRegistrationTimeGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/VoiceServices/VoiceService[Alias='VOICESERVICE1']/SIP/Clients/Client[Alias='CLIENT1']/LastRegistrationTime"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionServicesVoiceServicesVoiceServiceAliasVOICESERVICE1SIPClientsClientAliasCLIENT1GetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/VoiceServices/VoiceService[Alias='VOICESERVICE1']/SIP/Clients/Client[Alias='CLIENT1']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionUPnPDeviceUPnPIGDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/UPnP/Device/UPnPIGD"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionUPnPSettingsExtendedUPnPSecurityGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/UPnP/Settings/ExtendedUPnPSecurity"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionUserAccountsUsersUserLoginadminSecretQueryGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/UserAccounts/Users/User[Login='admin']/SecretQuery"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV0AssociatedDevicesGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/AssociatedDevices"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV0EnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV0SSIDAdvertisementEnabledGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/SSIDAdvertisementEnabled"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV0SecurityKeyPassphraseGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/Security/KeyPassphrase"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV0SecurityModeEnabledGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/Security/ModeEnabled"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV0SecurityModesSupportedGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/Security/ModesSupported"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV0SecurityWEPKeyGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/Security/WEPKey"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV0WPSEnableGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/WPS/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV1AssociatedDevicesGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/AssociatedDevices"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV1EnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV1SSIDAdvertisementEnabledGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/SSIDAdvertisementEnabled"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV1SecurityKeyPassphraseGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/Security/KeyPassphrase"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV1SecurityModeEnabledGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/Security/ModeEnabled"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV1SecurityModesSupportedGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/Security/ModesSupported"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV1SecurityWEPKeyGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/Security/WEPKey"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiAccessPointsAccessPointAliasPRIV1WPSEnableGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/WPS/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiQuantennaBootIPLocalGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Quantenna/BootIPLocal"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiQuantennaBootIPRemoteGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Quantenna/BootIPRemote"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiQuantennaMngtIPLocalGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Quantenna/MngtIPLocal"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiQuantennaMngtIPRemoteGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Quantenna/MngtIPRemote"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAutoChannelTriggerGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio/AutoChannelTrigger"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiRadiosRadioChannelSubscribeForNotification(HomeHubAction):
    def __init__(self, id):
        self.method = "subscribeForNotification"
        self.xpath = "Device/WiFi/Radios/Radio/Channel"
        self.parameters = {"id": id, "type": "value-change", "current-value": False}


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4AutoChannelEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/AutoChannelEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4AutoChannelTriggerGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/AutoChannelTrigger"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4ChannelGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/Channel"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4ChannelsInUseGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/ChannelsInUse"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4EnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4ExtensionChannelGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/ExtensionChannel"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4MaxBitRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/MaxBitRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4OperatingChannelBandwidthGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/OperatingChannelBandwidth"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4OperatingStandardsGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/OperatingStandards"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4PossibleChannelsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/PossibleChannels"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO2G4TransmitPowerGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/TransmitPower"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GAutoChannelEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/AutoChannelEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GAutoChannelTriggerGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/AutoChannelTrigger"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )
        self.admin_required = True


class HomeHubActionWiFiRadiosRadioAliasRADIO5GChannelGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/Channel"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GChannelsInUseGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/ChannelsInUse"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GExtensionChannelGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/ExtensionChannel"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GMaxBitRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/MaxBitRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GOperatingChannelBandwidthGetValue(
    HomeHubAction
):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/Radios/Radio[Alias='RADIO5G']/OperatingChannelBandwidth"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GOperatingStandardsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/OperatingStandards"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GPossibleChannelsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/PossibleChannels"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiRadiosRadioAliasRADIO5GTransmitPowerGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/TransmitPower"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID/Alias"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV2GConnectionTimeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV2G']/ConnectionTime"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV2GEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV2G']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV2GMACAddressGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV2G']/MACAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV2GSSIDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV2G']/SSID"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV2GStatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV2G']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV2GGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV2G']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV5GConnectionTimeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV5G']/ConnectionTime"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV5GEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV5G']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV5GMACAddressGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV5G']/MACAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV5GSSIDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV5G']/SSID"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV5GStatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV5G']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_PRIV5GGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV5G']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_REDSIDE_O1_2GSSIDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_REDSIDE_O1_2G']/SSID"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_REDSIDE_O1_5GSSIDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_REDSIDE_O1_5G']/SSID"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_REDSIDE_X1_2GSSIDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_REDSIDE_X1_2G']/SSID"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionWiFiSSIDsSSIDAliasWL_REDSIDE_X1_5GSSIDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_REDSIDE_X1_5G']/SSID"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionArping(HomeHubAction):
    def __init__(self):
        self.method = "arping"
        self.xpath = "Device"


class HomeHubActionLogIn(HomeHubAction):
    def __init__(self, user):
        self.method = "logIn"
        self.parameters = {
            "user": user,
            "persistent": "True",
            "session-options": {
                "nss": [{"name": "gtw", "uri": "http://sagemcom.com/gateway-data"}],
                "language": "ident",
                "context-flags": {"get-content-name": True, "local-time": True},
                "capability-depth": 2,
                "capability-flags": {
                    "name": True,
                    "default-value": False,
                    "restriction": True,
                    "description": False,
                },
                "time-format": "ISO_8601",
            },
        }


class HomeHubActionLogOut(HomeHubAction):
    def __init__(self):
        self.method = "logOut"


class HomeHubActionResetEvents(HomeHubAction):
    def __init__(self):
        self.method = "resetEvents"


class HomeHubActionUnsubscribeForNotification(HomeHubAction):
    def __init__(self, id):
        self.method = "unsubscribeForNotification"
        self.parameters = {"id": id}
