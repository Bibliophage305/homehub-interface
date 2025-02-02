from abc import ABC


class HomeHubActionBase(ABC):
    def as_dict(self):
        ret = {}
        for prop in self.dict_props:
            try:
                val = getattr(self, prop)
                if val is None:
                    continue
                elif isinstance(val, HomeHubActionBase):
                    ret[prop] = val.as_dict()
                else:
                    ret[prop] = val
            except AttributeError:
                continue
        return ret

    def __str__(self):
        return str(self.as_dict())


class HomeHubActionOptionsCapabilityFlags(HomeHubActionBase):
    dict_props = ["interface"]

    def __init__(self, interface: bool = None):
        self.interface = interface


class HomeHubActionOptions(HomeHubActionBase):
    dict_props = ["capability_flags"]

    def __init__(self, capability_flags: HomeHubActionOptionsCapabilityFlags = None):
        self.capability_flags = capability_flags


class HomeHubAction(HomeHubActionBase, ABC):
    admin_required = False

    dict_props = [
        "method",
        "xpath",
        "parameters",
        "options",
    ]

    def set_id(self, id: int):
        self.id = id


class MethodArpingMixin:
    method = "arping"


class MethodGetEventsMixin:
    method = "getEvents"


class MethodGetValueMixin:
    method = "getValue"


class MethodGetVendorLogDownloadURIMixin:
    method = "getVendorLogDownloadURI"


class MethodLogInMixin:
    method = "logIn"


class MethodLogOutMixin:
    method = "logOut"


class MethodResetEventsMixin:
    method = "resetEvents"


class MethodSetValueMixin:
    method = "setValue"


class MethodSubscribeForNotificationMixin:
    method = "subscribeForNotification"


class MethodUnsubscribeForNotificationMixin:
    method = "unsubscribeForNotification"


class MethodUploadBMStatisticsFileMixin:
    method = "uploadBMStatisticsFile"


optionsWithInterface = HomeHubActionOptions(
    capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
)


class OptionsInterfaceCapabilityMixin:
    options = optionsWithInterface


class AdminRequiredMixin:
    admin_required = True


from enum import Enum, auto


class HomeHubActionXPathParamAccessPointAlias(Enum):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionXPathParamChainName(Enum):
    Custom = auto()
    Low = auto()


class HomeHubActionXPathParamChannelAlias(Enum):
    DSL0 = auto()


class HomeHubActionXPathParamClientActive(Enum):
    true = auto()


class HomeHubActionXPathParamClientAlias(Enum):
    CLIENT1 = auto()


class HomeHubActionXPathParamForwardingStatus(Enum):
    ENABLED = auto()


class HomeHubActionXPathParamIPv4AddressAlias(Enum):
    IP_BR_OPENWIFI_ADDRESS = auto()
    IP_DATA_ADDRESS = auto()


class HomeHubActionXPathParamIPv6AddressAlias(Enum):
    LINK_LOCAL = auto()
    ULA_LAN = auto()


class HomeHubActionXPathParamIPv6AddressIPAddressStatus(Enum):
    PREFERRED = auto()


class HomeHubActionXPathParamIPv6PrefixAlias(Enum):
    ULA_LAN = auto()


class HomeHubActionXPathParamInterfaceAlias(Enum):
    IP_BR_LAN = auto()
    IP_BR_OPENWIFI = auto()
    IP_DATA = auto()
    PHY1 = auto()
    PHY4 = auto()
    PHY6_WAN = auto()
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionXPathParamInterfaceSettingAlias(Enum):
    RA_BR_LAN = auto()


class HomeHubActionXPathParamLevelName(Enum):
    Custom = auto()


class HomeHubActionXPathParamLineAlias(Enum):
    DSL0 = auto()
    LINE1 = auto()


class HomeHubActionXPathParamLinkAlias(Enum):
    ATM_DATA = auto()
    ATM_TV = auto()
    FTTH_DATA = auto()


class HomeHubActionXPathParamPoolAlias(Enum):
    DEFAULT_POOL = auto()
    OPENWIFI_POOL = auto()


class HomeHubActionXPathParamPortMappingAlias(Enum):
    API_DMZ = auto()


class HomeHubActionXPathParamPortMappingService(Enum):
    DMZ = auto()


class HomeHubActionXPathParamRadioAlias(Enum):
    RADIO2G4 = auto()
    RADIO5G = auto()


class HomeHubActionXPathParamSSIDAlias(Enum):
    WL_PRIV2G = auto()
    WL_PRIV5G = auto()
    WL_REDSIDE_O1_2G = auto()
    WL_REDSIDE_O1_5G = auto()
    WL_REDSIDE_X1_2G = auto()
    WL_REDSIDE_X1_5G = auto()


class HomeHubActionXPathParamUserLogin(Enum):
    admin = auto()


class HomeHubActionXPathParamVLANTerminationAlias(Enum):
    VLAN_DATA = auto()


class HomeHubActionXPathParamVoiceServiceAlias(Enum):
    VOICESERVICE1 = auto()


class HomeHubActionDeviceATMLinksLinkParamAliasDestinationAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, link_alias: HomeHubActionXPathParamLinkAlias):
        self.link_alias = link_alias

    @property
    def xpath(self):
        return (
            f"Device/ATM/Links/Link[Alias='{self.link_alias.name}']/DestinationAddress"
        )


class HomeHubActionDeviceDHCPv4ServerPoolsPoolParamAliasEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Enable"


class HomeHubActionDeviceDHCPv4ServerPoolsPoolParamAliasIPInterfaceGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/IPInterface"


class HomeHubActionDeviceDHCPv4ServerPoolsPoolParamAliasLeaseTimeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return (
            f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/LeaseTime"
        )


class HomeHubActionDeviceDHCPv4ServerPoolsPoolParamAliasMaxAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/MaxAddress"


class HomeHubActionDeviceDHCPv4ServerPoolsPoolParamAliasMinAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/MinAddress"


class HomeHubActionDeviceDHCPv4ServerPoolsPoolParamAliasStaticAddressesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/StaticAddresses"


class HomeHubActionDeviceDHCPv4ServerPoolsPoolParamAliasSubnetMaskGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/SubnetMask"


class HomeHubActionDeviceDHCPv4ServerX_SAGEMCOM_AuthoritativeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DHCPv4/Server/X_SAGEMCOM_Authoritative"


class HomeHubActionDeviceDHCPv6ServerPoolsPoolParamAliasClientsClientParamActiveIPv6AddressesIPv6AddressIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        pool_alias: HomeHubActionXPathParamPoolAlias,
        client_active: HomeHubActionXPathParamClientActive,
    ):
        self.pool_alias = pool_alias
        self.client_active = client_active

    @property
    def xpath(self):
        return f"Device/DHCPv6/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Clients/Client[Active='{self.client_active.name}']/IPv6Addresses/IPv6Address/IPAddress"


class HomeHubActionDeviceDHCPv6ServerPoolsPoolParamAliasIANAEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv6/Server/Pools/Pool[Alias='{self.pool_alias.name}']/IANAEnable"


class HomeHubActionDeviceDHCPv6ServerPoolsPoolParamAliasStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv6/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Status"


class HomeHubActionDeviceDNSClientHostNameGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DNS/Client/HostName"


class HomeHubActionDeviceDNSClientLocalDomainsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DNS/Client/LocalDomains"


class HomeHubActionDeviceDNSRelayForwardingsForwardingParamStatusDNSServerGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, forwarding_status: HomeHubActionXPathParamForwardingStatus):
        self.forwarding_status = forwarding_status

    @property
    def xpath(self):
        return f"Device/DNS/Relay/Forwardings/Forwarding[Status='{self.forwarding_status.name}']/DNSServer"


class HomeHubActionDeviceDNSRelayLocalDomainsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DNS/Relay/LocalDomains"


class HomeHubActionDeviceDSLChannelsChannelParamuidDownstreamCurrRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, channel_uid: int):
        self.channel_uid = channel_uid

    @property
    def xpath(self):
        return (
            f"Device/DSL/Channels/Channel[@uid='{self.channel_uid}']/DownstreamCurrRate"
        )


class HomeHubActionDeviceDSLChannelsChannelParamuidUpstreamCurrRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, channel_uid: int):
        self.channel_uid = channel_uid

    @property
    def xpath(self):
        return (
            f"Device/DSL/Channels/Channel[@uid='{self.channel_uid}']/UpstreamCurrRate"
        )


class HomeHubActionDeviceDSLChannelsChannelParamAliasActualInterleavingDelayGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, channel_alias: HomeHubActionXPathParamChannelAlias):
        self.channel_alias = channel_alias

    @property
    def xpath(self):
        return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/ActualInterleavingDelay"


class HomeHubActionDeviceDSLChannelsChannelParamAliasActualInterleavingDelayusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, channel_alias: HomeHubActionXPathParamChannelAlias):
        self.channel_alias = channel_alias

    @property
    def xpath(self):
        return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/ActualInterleavingDelayus"


class HomeHubActionDeviceDSLChannelsChannelParamAliasDownstreamCurrRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, channel_alias: HomeHubActionXPathParamChannelAlias):
        self.channel_alias = channel_alias

    @property
    def xpath(self):
        return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/DownstreamCurrRate"


class HomeHubActionDeviceDSLChannelsChannelParamAliasUpstreamCurrRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, channel_alias: HomeHubActionXPathParamChannelAlias):
        self.channel_alias = channel_alias

    @property
    def xpath(self):
        return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/UpstreamCurrRate"


class HomeHubActionDeviceDSLLinesLineParamuidLastChangeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_uid: int):
        self.line_uid = line_uid

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/LastChange"


class HomeHubActionDeviceDSLLinesLineParamuidStatsBytesReceivedGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_uid: int):
        self.line_uid = line_uid

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/Stats/BytesReceived"


class HomeHubActionDeviceDSLLinesLineParamuidStatsBytesSentGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_uid: int):
        self.line_uid = line_uid

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/Stats/BytesSent"


class HomeHubActionDeviceDSLLinesLineParamAliasDownstreamAttenuationGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamAttenuation"


class HomeHubActionDeviceDSLLinesLineParamAliasDownstreamMaxBitRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamMaxBitRate"


class HomeHubActionDeviceDSLLinesLineParamAliasDownstreamNoiseMarginGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamNoiseMargin"


class HomeHubActionDeviceDSLLinesLineParamAliasFirmwareVersionGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/FirmwareVersion"


class HomeHubActionDeviceDSLLinesLineParamAliasLastChangeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/LastChange"


class HomeHubActionDeviceDSLLinesLineParamAliasSignalDownstreamAttenuationGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/SignalDownstreamAttenuation"


class HomeHubActionDeviceDSLLinesLineParamAliasSignalUpstreamAttenuationGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/SignalUpstreamAttenuation"


class HomeHubActionDeviceDSLLinesLineParamAliasStandardUsedGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/StandardUsed"


class HomeHubActionDeviceDSLLinesLineParamAliasStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/Status"


class HomeHubActionDeviceDSLLinesLineParamAliasUpstreamAttenuationGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return (
            f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/UpstreamAttenuation"
        )


class HomeHubActionDeviceDSLLinesLineParamAliasUpstreamMaxBitRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return (
            f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/UpstreamMaxBitRate"
        )


class HomeHubActionDeviceDSLLinesLineParamAliasUpstreamNoiseMarginGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return (
            f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/UpstreamNoiseMargin"
        )


class HomeHubActionDeviceDeviceDiscoveryDeviceIdentificationDeviceTypesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceDiscovery/DeviceIdentification/DeviceTypes"


class HomeHubActionDeviceDeviceInfoBootloaderVersionGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/BootloaderVersion"


class HomeHubActionDeviceDeviceInfoExternalFirmwareVersionGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/ExternalFirmwareVersion"


class HomeHubActionDeviceDeviceInfoHardwareVersionGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/HardwareVersion"


class HomeHubActionDeviceDeviceInfoMACAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/MACAddress"


class HomeHubActionDeviceDeviceInfoModelNameGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/ModelName"


class HomeHubActionDeviceDeviceInfoProductClassGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/ProductClass"


class HomeHubActionDeviceDeviceInfoProductVariantGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/ProductVariant"


class HomeHubActionDeviceDeviceInfoSerialNumberGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/SerialNumber"


class HomeHubActionDeviceDeviceInfoSupportedDataModelsSupportedDataModelURLGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/SupportedDataModels/SupportedDataModel/URL"


class HomeHubActionDeviceDeviceInfoUpTimeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DeviceInfo/UpTime"


class HomeHubActionDeviceDeviceInfoVendorLogFilesVendorLogFileParamuidGetVendorLogDownloadURI(
    HomeHubAction, MethodGetVendorLogDownloadURIMixin
):
    def __init__(self, vendorlogfile_uid: int):
        self.vendorlogfile_uid = vendorlogfile_uid

    @property
    def xpath(self):
        return f"Device/DeviceInfo/VendorLogFiles/VendorLogFile[@uid='{self.vendorlogfile_uid}']"

    parameters = {"FileName": "eventLog"}


class HomeHubActionDeviceEthernetInterfacesInterfaceParamAliasStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/Ethernet/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


class HomeHubActionDeviceEthernetInterfacesInterfaceParamAliasMACAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/Ethernet/Interfaces/Interface[Alias='{self.interface_alias.name}']/MACAddress"


class HomeHubActionDeviceEthernetLinksLinkParamAliasLowerLayersGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, link_alias: HomeHubActionXPathParamLinkAlias):
        self.link_alias = link_alias

    @property
    def xpath(self):
        return f"Device/Ethernet/Links/Link[Alias='{self.link_alias.name}']/LowerLayers"


class HomeHubActionDeviceEthernetVLANTerminationsVLANTerminationParamAliasVLANIDGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, vlantermination_alias: HomeHubActionXPathParamVLANTerminationAlias
    ):
        self.vlantermination_alias = vlantermination_alias

    @property
    def xpath(self):
        return f"Device/Ethernet/VLANTerminations/VLANTermination[Alias='{self.vlantermination_alias.name}']/VLANID"


class HomeHubActionDeviceFASTLinesLineParamuidStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_uid: int):
        self.line_uid = line_uid

    @property
    def xpath(self):
        return f"Device/FAST/Lines/Line[@uid='{self.line_uid}']/Status"


class HomeHubActionDeviceFirewallChainsChainParamNameRulesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, chain_name: HomeHubActionXPathParamChainName):
        self.chain_name = chain_name

    @property
    def xpath(self):
        return f"Device/Firewall/Chains/Chain[Name='{self.chain_name.name}']/Rules"


class HomeHubActionDeviceFirewallChainsChainParamNameRulesRuleParamIPVersionGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, chain_name: HomeHubActionXPathParamChainName, rule_ipversion: int
    ):
        self.chain_name = chain_name
        self.rule_ipversion = rule_ipversion

    @property
    def xpath(self):
        return f"Device/Firewall/Chains/Chain[Name='{self.chain_name.name}']/Rules/Rule[IPVersion='{self.rule_ipversion}']"


class HomeHubActionDeviceFirewallConfigGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Firewall/Config"


class HomeHubActionDeviceFirewallEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Firewall/Enable"


class HomeHubActionDeviceFirewallLevelsLevelParamNameDefaultPolicyGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, level_name: HomeHubActionXPathParamLevelName):
        self.level_name = level_name

    @property
    def xpath(self):
        return (
            f"Device/Firewall/Levels/Level[Name='{self.level_name.name}']/DefaultPolicy"
        )


class HomeHubActionDeviceFirewallRespondToPingGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Firewall/RespondToPing"


class HomeHubActionDeviceHostsHistoryMaxAgeInDaysGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Hosts/HistoryMaxAgeInDays"


class HomeHubActionDeviceHostsHostsHostBlacklistedScheduleGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Hosts/Hosts/Host/BlacklistedSchedule"


class HomeHubActionDeviceHostsHostsHostParamuidGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, host_uid: int):
        self.host_uid = host_uid

    @property
    def xpath(self):
        return f"Device/Hosts/Hosts/Host[@uid='{self.host_uid}']"


class HomeHubActionDeviceHostsHostsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Hosts/Hosts"


class HomeHubActionDeviceIPIPv6StatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/IP/IPv6Status"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv6AddressesIPv6AddressIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address/IPAddress"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv6AddressesIPv6AddressParamAliasIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionXPathParamInterfaceAlias,
        ipv6address_alias: HomeHubActionXPathParamIPv6AddressAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv6address_alias = ipv6address_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address[Alias='{self.ipv6address_alias.name}']/IPAddress"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv6AddressesIPv6AddressParamIPAddressStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionXPathParamInterfaceAlias,
        ipv6address_ipaddressstatus: HomeHubActionXPathParamIPv6AddressIPAddressStatus,
    ):
        self.interface_alias = interface_alias
        self.ipv6address_ipaddressstatus = ipv6address_ipaddressstatus

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address[IPAddressStatus='{self.ipv6address_ipaddressstatus.name}']"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv6PrefixesIPv6PrefixParamAliasPrefixGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionXPathParamInterfaceAlias,
        ipv6prefix_alias: HomeHubActionXPathParamIPv6PrefixAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv6prefix_alias = ipv6prefix_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Prefixes/IPv6Prefix[Alias='{self.ipv6prefix_alias.name}']/Prefix"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv6PrefixesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Prefixes"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasULAEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/ULAEnable"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv4AddressesIPv4AddressParamAliasIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionXPathParamInterfaceAlias,
        ipv4address_alias: HomeHubActionXPathParamIPv4AddressAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv4address_alias = ipv4address_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/IPAddress"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv4AddressesIPv4AddressParamAliasSubnetMaskGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionXPathParamInterfaceAlias,
        ipv4address_alias: HomeHubActionXPathParamIPv4AddressAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv4address_alias = ipv4address_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/SubnetMask"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv4AddressesIPv4AddressIPGatewayGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address/IPGateway"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasIPv4AddressesIPv4AddressParamAliasDnsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionXPathParamInterfaceAlias,
        ipv4address_alias: HomeHubActionXPathParamIPv4AddressAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv4address_alias = ipv4address_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/Dns"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasLastChangeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/LastChange"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasStatsBytesReceivedGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Stats/BytesReceived"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasStatsBytesSentGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Stats/BytesSent"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


class HomeHubActionDeviceIPInterfacesInterfaceParamAliasStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias, id: int):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    @property
    def parameters(self):
        return {"id": self.id, "type": "value-change", "current-value": False}


class HomeHubActionDeviceManagementServerTR69InternalDataSettingsPortGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/ManagementServer/TR69InternalData/Settings/Port"


class HomeHubActionDeviceManagersHubLightControlBrightnessGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/HubLightControl/Brightness"


class HomeHubActionDeviceManagersHubLightControlBrightnessSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/HubLightControl/Brightness"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceManagersHubLightControlFrontLEDColorGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/HubLightControl/FrontLEDColor"


class HomeHubActionDeviceManagersHubLightControlLedEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/HubLightControl/LedEnable"


class HomeHubActionDeviceManagersHubLightControlLedEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/HubLightControl/LedEnable"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceManagersHubLightControlScheduleEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/HubLightControl/Schedule/Enable"


class HomeHubActionDeviceManagersHubLightControlScheduleEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/HubLightControl/Schedule/Enable"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceManagersHubLightControlScheduleTurnLightOffGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOff"


class HomeHubActionDeviceManagersHubLightControlScheduleTurnLightOffSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOff"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceManagersHubLightControlScheduleTurnLightOnGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOn"


class HomeHubActionDeviceManagersHubLightControlScheduleTurnLightOnSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOn"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceManagersNetworkDataDhcpLanMaxAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/NetworkData/DhcpLanMaxAddress"


class HomeHubActionDeviceManagersNetworkDataDhcpLanMinAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/NetworkData/DhcpLanMinAddress"


class HomeHubActionDeviceManagersNetworkDataIPv6ModeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/NetworkData/IPv6Mode"


class HomeHubActionDeviceManagersNetworkDataIpLanGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/NetworkData/IpLan"


class HomeHubActionDeviceManagersNetworkDataNetmaskLanGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/NetworkData/NetmaskLan"


class HomeHubActionDeviceManagersNetworkDataObfuscatedPPPPasswordGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Managers/NetworkData/ObfuscatedPPPPassword"


class HomeHubActionDeviceManagersNetworkDataObfuscatedPPPPasswordSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/NetworkData/ObfuscatedPPPPassword"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceNATPortMappingsPortMappingParamAliasInternalClientGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, portmapping_alias: HomeHubActionXPathParamPortMappingAlias):
        self.portmapping_alias = portmapping_alias

    @property
    def xpath(self):
        return f"Device/NAT/PortMappings/PortMapping[Alias='{self.portmapping_alias.name}']/InternalClient"


class HomeHubActionDeviceNATPortMappingsPortMappingParamAliasInternalMACAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, portmapping_alias: HomeHubActionXPathParamPortMappingAlias):
        self.portmapping_alias = portmapping_alias

    @property
    def xpath(self):
        return f"Device/NAT/PortMappings/PortMapping[Alias='{self.portmapping_alias.name}']/InternalMACAddress"


class HomeHubActionDeviceNATPortMappingsPortMappingParamServiceEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, portmapping_service: HomeHubActionXPathParamPortMappingService):
        self.portmapping_service = portmapping_service

    @property
    def xpath(self):
        return f"Device/NAT/PortMappings/PortMapping[Service='{self.portmapping_service.name}']/Enable"


class HomeHubActionDeviceNATPortMappingsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/NAT/PortMappings"


class HomeHubActionDeviceNATSIPALGEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/NAT/SIPALGEnable"


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasConnectionStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/ConnectionStatus"


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasIPCPLocalIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPCP/LocalIPAddress"


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasIPCPRemoteIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPCP/RemoteIPAddress"


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasIPv6CPRemoteInterfaceIdentifierGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6CP/RemoteInterfaceIdentifier"


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Enable"


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(
        self, interface_alias: HomeHubActionXPathParamInterfaceAlias, value: any
    ):
        self.interface_alias = interface_alias
        self.value = value

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Enable"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias, id: int):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    @property
    def parameters(self):
        return {"id": self.id, "type": "value-change", "current-value": False}


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasUsernameGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Username"


class HomeHubActionDevicePPPInterfacesInterfaceParamAliasUsernameSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(
        self, interface_alias: HomeHubActionXPathParamInterfaceAlias, value: any
    ):
        self.interface_alias = interface_alias
        self.value = value

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Username"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceRouterAdvertisementInterfaceSettingsInterfaceSettingParamAliasAdvManagedFlagGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, interfacesetting_alias: HomeHubActionXPathParamInterfaceSettingAlias
    ):
        self.interfacesetting_alias = interfacesetting_alias

    @property
    def xpath(self):
        return f"Device/RouterAdvertisement/InterfaceSettings/InterfaceSetting[Alias='{self.interfacesetting_alias.name}']/AdvManagedFlag"


class HomeHubActionDeviceRouterAdvertisementInterfaceSettingsInterfaceSettingParamAliasAdvOtherConfigFlagGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, interfacesetting_alias: HomeHubActionXPathParamInterfaceSettingAlias
    ):
        self.interfacesetting_alias = interfacesetting_alias

    @property
    def xpath(self):
        return f"Device/RouterAdvertisement/InterfaceSettings/InterfaceSetting[Alias='{self.interfacesetting_alias.name}']/AdvOtherConfigFlag"


class HomeHubActionDeviceServicesBandwidthMonitoringUploadBMStatisticsFile(
    HomeHubAction, MethodUploadBMStatisticsFileMixin
):
    xpath = "Device/Services/BandwidthMonitoring"

    parameters = {"startDate": "20000101", "endDate": "20250122"}


class HomeHubActionDeviceServicesBusinessDNSOverrideServersGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/Business/DNSOverrideServers"


class HomeHubActionDeviceServicesBusinessDNSOverrideGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/Business/DNSOverride"


class HomeHubActionDeviceServicesBusinessStaticIPAddressAssignationsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/Business/staticIP/AddressAssignations"


class HomeHubActionDeviceServicesBusinessStaticIPRoutedLANEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/Business/staticIP/RoutedLANEnable"


class HomeHubActionDeviceServicesDeviceConfigConnectionHURLPageEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/ConnectionHURLPageEnable"


class HomeHubActionDeviceServicesDeviceConfigDomainLockListGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/DomainLockList"


class HomeHubActionDeviceServicesDeviceConfigDomainLockingEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/DomainLockingEnable"


class HomeHubActionDeviceServicesDeviceConfigEnableBridgedModeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/EnableBridgedMode"


class HomeHubActionDeviceServicesDeviceConfigLastFirmwareUpgradeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/LastFirmwareUpgrade"


class HomeHubActionDeviceServicesDeviceConfigLastSuccesfulWanTypeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/LastSuccesfulWanType"


class HomeHubActionDeviceServicesDeviceConfigPortClampingEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/PortClampingEnable"


class HomeHubActionDeviceServicesDeviceConfigPortClampingEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Services/DeviceConfig/PortClampingEnable"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceServicesDeviceConfigWiFiModeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/WiFiMode"


class HomeHubActionDeviceServicesDeviceConfigWifiPasswordForbiddenWordsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/WifiPasswordForbiddenWords"


class HomeHubActionDeviceServicesDynamicDNSClientsClientParamuidEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Enable"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceServicesDynamicDNSClientsClientParamuidHostnamesHostnameParamuidNameSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, hostname_uid: int, value: any):
        self.client_uid = client_uid
        self.hostname_uid = hostname_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Hostnames/Hostname[@uid='{self.hostname_uid}']/Name"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceServicesDynamicDNSClientsClientParamuidPasswordSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Password"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceServicesDynamicDNSClientsClientParamuidServiceReferenceSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/ServiceReference"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceServicesDynamicDNSClientsClientParamuidUsernameSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Username"

    @property
    def parameters(self):
        return {
            "value": self.value,
        }


class HomeHubActionDeviceServicesDynamicDNSClientsClientParamuidGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, client_uid: int):
        self.client_uid = client_uid

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']"


class HomeHubActionDeviceServicesDynamicDNSServicesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DynamicDNS/Services"


class HomeHubActionDeviceServicesOnlineInstallDHCPFingerprintDatabaseEntriesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/OnlineInstall/DHCPFingerprintDatabase/Entries"


class HomeHubActionDeviceServicesOnlineInstallEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/OnlineInstall/Enable"


class HomeHubActionDeviceServicesOpenWiFiOpenWifiOptedInGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/OpenWiFi/OpenWifiOptedIn"


class HomeHubActionDeviceServicesOpenWiFiUIEnabledGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/OpenWiFi/UIEnabled"


class HomeHubActionDeviceServicesParentalControlGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/ParentalControl"


class HomeHubActionDeviceServicesStorageServicesStorageServiceParamuidLogicalVolumesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, storageservice_uid: int):
        self.storageservice_uid = storageservice_uid

    @property
    def xpath(self):
        return f"Device/Services/StorageServices/StorageService[@uid='{self.storageservice_uid}']/LogicalVolumes"


class HomeHubActionDeviceServicesVoiceServicesVoiceServiceParamAliasCallControlLinesLineParamAliasGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        voiceservice_alias: HomeHubActionXPathParamVoiceServiceAlias,
        line_alias: HomeHubActionXPathParamLineAlias,
    ):
        self.voiceservice_alias = voiceservice_alias
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/CallControl/Lines/Line[Alias='{self.line_alias.name}']"


class HomeHubActionDeviceServicesVoiceServicesVoiceServiceParamAliasCallLogsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, voiceservice_alias: HomeHubActionXPathParamVoiceServiceAlias):
        self.voiceservice_alias = voiceservice_alias

    @property
    def xpath(self):
        return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/CallLogs"


class HomeHubActionDeviceServicesVoiceServicesVoiceServiceParamAliasSIPClientsClientParamAliasLastRegistrationTimeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        voiceservice_alias: HomeHubActionXPathParamVoiceServiceAlias,
        client_alias: HomeHubActionXPathParamClientAlias,
    ):
        self.voiceservice_alias = voiceservice_alias
        self.client_alias = client_alias

    @property
    def xpath(self):
        return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/SIP/Clients/Client[Alias='{self.client_alias.name}']/LastRegistrationTime"


class HomeHubActionDeviceServicesVoiceServicesVoiceServiceParamAliasSIPClientsClientParamAliasGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        voiceservice_alias: HomeHubActionXPathParamVoiceServiceAlias,
        client_alias: HomeHubActionXPathParamClientAlias,
    ):
        self.voiceservice_alias = voiceservice_alias
        self.client_alias = client_alias

    @property
    def xpath(self):
        return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/SIP/Clients/Client[Alias='{self.client_alias.name}']"


class HomeHubActionDeviceUPnPDeviceUPnPIGDGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/UPnP/Device/UPnPIGD"


class HomeHubActionDeviceUPnPSettingsExtendedUPnPSecurityGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/UPnP/Settings/ExtendedUPnPSecurity"


class HomeHubActionDeviceUserAccountsUsersUserParamLoginSecretQueryGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, user_login: HomeHubActionXPathParamUserLogin):
        self.user_login = user_login

    @property
    def xpath(self):
        return f"Device/UserAccounts/Users/User[Login='{self.user_login.name}']/SecretQuery"


class HomeHubActionDeviceWiFiAccessPointsAccessPointParamAliasAssociatedDevicesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/AssociatedDevices"


class HomeHubActionDeviceWiFiAccessPointsAccessPointParamAliasEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Enable"


class HomeHubActionDeviceWiFiAccessPointsAccessPointParamAliasSSIDAdvertisementEnabledGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/SSIDAdvertisementEnabled"


class HomeHubActionDeviceWiFiAccessPointsAccessPointParamAliasSecurityKeyPassphraseGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/KeyPassphrase"


class HomeHubActionDeviceWiFiAccessPointsAccessPointParamAliasSecurityModeEnabledGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/ModeEnabled"


class HomeHubActionDeviceWiFiAccessPointsAccessPointParamAliasSecurityModesSupportedGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/ModesSupported"


class HomeHubActionDeviceWiFiAccessPointsAccessPointParamAliasSecurityWEPKeyGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/WEPKey"


class HomeHubActionDeviceWiFiAccessPointsAccessPointParamAliasWPSEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/WPS/Enable"


class HomeHubActionDeviceWiFiQuantennaBootIPLocalGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/WiFi/Quantenna/BootIPLocal"


class HomeHubActionDeviceWiFiQuantennaBootIPRemoteGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/WiFi/Quantenna/BootIPRemote"


class HomeHubActionDeviceWiFiQuantennaMngtIPLocalGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/WiFi/Quantenna/MngtIPLocal"


class HomeHubActionDeviceWiFiQuantennaMngtIPRemoteGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/WiFi/Quantenna/MngtIPRemote"


class HomeHubActionDeviceWiFiRadiosRadioAutoChannelTriggerGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/WiFi/Radios/Radio/AutoChannelTrigger"


class HomeHubActionDeviceWiFiRadiosRadioChannelSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(self, id: int):
        self.id = id

    xpath = "Device/WiFi/Radios/Radio/Channel"

    @property
    def parameters(self):
        return {"id": self.id, "type": "value-change", "current-value": False}


class HomeHubActionDeviceWiFiRadiosRadioParamAliasAutoChannelEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/AutoChannelEnable"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasAutoChannelTriggerGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/AutoChannelTrigger"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasChannelGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/Channel"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasChannelsInUseGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return (
            f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/ChannelsInUse"
        )


class HomeHubActionDeviceWiFiRadiosRadioParamAliasEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/Enable"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasExtensionChannelGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/ExtensionChannel"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasMaxBitRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/MaxBitRate"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasOperatingChannelBandwidthGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/OperatingChannelBandwidth"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasOperatingStandardsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/OperatingStandards"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasPossibleChannelsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/PossibleChannels"


class HomeHubActionDeviceWiFiRadiosRadioParamAliasTransmitPowerGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return (
            f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/TransmitPower"
        )


class HomeHubActionDeviceWiFiSSIDsSSIDAliasGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/WiFi/SSIDs/SSID/Alias"


class HomeHubActionDeviceWiFiSSIDsSSIDParamAliasConnectionTimeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/ConnectionTime"


class HomeHubActionDeviceWiFiSSIDsSSIDParamAliasEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/Enable"


class HomeHubActionDeviceWiFiSSIDsSSIDParamAliasMACAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/MACAddress"


class HomeHubActionDeviceWiFiSSIDsSSIDParamAliasSSIDGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/SSID"


class HomeHubActionDeviceWiFiSSIDsSSIDParamAliasStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/Status"


class HomeHubActionDeviceWiFiSSIDsSSIDParamAliasGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']"


class HomeHubActionDeviceArping(HomeHubAction, MethodArpingMixin):
    xpath = "Device"


class HomeHubActionGetEvents(HomeHubAction, MethodGetEventsMixin):
    pass


class HomeHubActionLogIn(HomeHubAction, MethodLogInMixin):
    def __init__(self, user: str):
        self.user = user

    @property
    def parameters(self):
        return {
            "user": self.user,
            "persistent": True,
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


class HomeHubActionLogOut(HomeHubAction, MethodLogOutMixin):
    pass


class HomeHubActionResetEvents(HomeHubAction, MethodResetEventsMixin):
    pass


class HomeHubActionUnsubscribeForNotification(
    HomeHubAction, MethodUnsubscribeForNotificationMixin
):
    def __init__(self, id: int):
        self.id = id

    @property
    def parameters(self):
        return {
            "id": self.id,
        }
