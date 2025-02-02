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


class HomeHubActionDeviceATMLinksDestinationAddressGetValueLinkAlias(Enum):
    ATM_TV = auto()
    ATM_DATA = auto()


class HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValuePoolAlias(Enum):
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValuePoolAlias(Enum):
    OPENWIFI_POOL = auto()
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValuePoolAlias(Enum):
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv4ServerPoolsMaxAddressGetValuePoolAlias(Enum):
    OPENWIFI_POOL = auto()
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv4ServerPoolsMinAddressGetValuePoolAlias(Enum):
    OPENWIFI_POOL = auto()
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv4ServerPoolsStaticAddressesGetValuePoolAlias(Enum):
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv4ServerPoolsSubnetMaskGetValuePoolAlias(Enum):
    OPENWIFI_POOL = auto()
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv6ServerPoolsClientsIPv6AddressesIPv6AddressIPAddressGetValuePoolAlias(
    Enum
):
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv6ServerPoolsClientsIPv6AddressesIPv6AddressIPAddressGetValueClientActive(
    Enum
):
    true = auto()


class HomeHubActionDeviceDHCPv6ServerPoolsIANAEnableGetValuePoolAlias(Enum):
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDHCPv6ServerPoolsStatusGetValuePoolAlias(Enum):
    DEFAULT_POOL = auto()


class HomeHubActionDeviceDNSRelayForwardingsDNSServerGetValueForwardingStatus(Enum):
    ENABLED = auto()


class HomeHubActionDeviceDSLChannelsActualInterleavingDelayGetValueChannelAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLChannelsActualInterleavingDelayusGetValueChannelAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLChannelsDownstreamCurrRateGetValueChannelAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLChannelsUpstreamCurrRateGetValueChannelAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesDownstreamAttenuationGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesDownstreamMaxBitRateGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesDownstreamNoiseMarginGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesFirmwareVersionGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesLastChangeGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesSignalDownstreamAttenuationGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesSignalUpstreamAttenuationGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesStandardUsedGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesStatusGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesUpstreamAttenuationGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesUpstreamMaxBitRateGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceDSLLinesUpstreamNoiseMarginGetValueLineAlias(Enum):
    DSL0 = auto()


class HomeHubActionDeviceEthernetInterfacesStatusGetValueInterfaceAlias(Enum):
    PHY4 = auto()
    PHY6_WAN = auto()


class HomeHubActionDeviceEthernetInterfacesMACAddressGetValueInterfaceAlias(Enum):
    PHY1 = auto()


class HomeHubActionDeviceEthernetLinksLowerLayersGetValueLinkAlias(Enum):
    FTTH_DATA = auto()


class HomeHubActionDeviceEthernetVLANTerminationsVLANIDGetValueVLANTerminationAlias(
    Enum
):
    VLAN_DATA = auto()


class HomeHubActionDeviceFirewallChainsRulesGetValueChainName(Enum):
    Custom = auto()
    Low = auto()


class HomeHubActionDeviceFirewallLevelsDefaultPolicyGetValueLevelName(Enum):
    Custom = auto()


class HomeHubActionDeviceIPInterfacesIPv6AddressesIPv6AddressIPAddressGetValueInterfaceAlias(
    Enum
):
    IP_BR_LAN = auto()


class HomeHubActionDeviceIPInterfacesIPv6AddressesIPAddressGetValueInterfaceAlias(Enum):
    IP_DATA = auto()
    IP_BR_LAN = auto()


class HomeHubActionDeviceIPInterfacesIPv6AddressesIPAddressGetValueIPv6AddressAlias(
    Enum
):
    LINK_LOCAL = auto()
    ULA_LAN = auto()


class HomeHubActionDeviceIPInterfacesIPv6AddressesGetValueInterfaceAlias(Enum):
    IP_DATA = auto()
    IP_BR_LAN = auto()


class HomeHubActionDeviceIPInterfacesIPv6AddressesGetValueIPv6AddressIPAddressStatus(
    Enum
):
    PREFERRED = auto()


class HomeHubActionDeviceIPInterfacesIPv6PrefixesPrefixGetValueInterfaceAlias(Enum):
    IP_BR_LAN = auto()


class HomeHubActionDeviceIPInterfacesIPv6PrefixesPrefixGetValueIPv6PrefixAlias(Enum):
    ULA_LAN = auto()


class HomeHubActionDeviceIPInterfacesIPv6PrefixesGetValueInterfaceAlias(Enum):
    IP_DATA = auto()
    IP_BR_LAN = auto()


class HomeHubActionDeviceIPInterfacesULAEnableGetValueInterfaceAlias(Enum):
    IP_BR_LAN = auto()


class HomeHubActionDeviceIPInterfacesIPv4AddressesIPAddressGetValueInterfaceAlias(Enum):
    IP_DATA = auto()
    IP_BR_OPENWIFI = auto()


class HomeHubActionDeviceIPInterfacesIPv4AddressesIPAddressGetValueIPv4AddressAlias(
    Enum
):
    IP_DATA_ADDRESS = auto()
    IP_BR_OPENWIFI_ADDRESS = auto()


class HomeHubActionDeviceIPInterfacesIPv4AddressesSubnetMaskGetValueInterfaceAlias(
    Enum
):
    IP_DATA = auto()
    IP_BR_OPENWIFI = auto()


class HomeHubActionDeviceIPInterfacesIPv4AddressesSubnetMaskGetValueIPv4AddressAlias(
    Enum
):
    IP_DATA_ADDRESS = auto()
    IP_BR_OPENWIFI_ADDRESS = auto()


class HomeHubActionDeviceIPInterfacesIPv4AddressesIPv4AddressIPGatewayGetValueInterfaceAlias(
    Enum
):
    IP_DATA = auto()


class HomeHubActionDeviceIPInterfacesIPv4AddressesDnsGetValueInterfaceAlias(Enum):
    IP_DATA = auto()


class HomeHubActionDeviceIPInterfacesIPv4AddressesDnsGetValueIPv4AddressAlias(Enum):
    IP_DATA_ADDRESS = auto()


class HomeHubActionDeviceIPInterfacesLastChangeGetValueInterfaceAlias(Enum):
    IP_DATA = auto()


class HomeHubActionDeviceIPInterfacesStatsBytesReceivedGetValueInterfaceAlias(Enum):
    IP_DATA = auto()


class HomeHubActionDeviceIPInterfacesStatsBytesSentGetValueInterfaceAlias(Enum):
    IP_DATA = auto()


class HomeHubActionDeviceIPInterfacesStatusGetValueInterfaceAlias(Enum):
    IP_DATA = auto()


class HomeHubActionDeviceIPInterfacesStatusSubscribeForNotificationInterfaceAlias(Enum):
    IP_DATA = auto()


class HomeHubActionDeviceNATPortMappingsInternalClientGetValuePortMappingAlias(Enum):
    API_DMZ = auto()


class HomeHubActionDeviceNATPortMappingsInternalMACAddressGetValuePortMappingAlias(
    Enum
):
    API_DMZ = auto()


class HomeHubActionDeviceNATPortMappingsEnableGetValuePortMappingService(Enum):
    DMZ = auto()


class HomeHubActionDevicePPPInterfacesConnectionStatusGetValueInterfaceAlias(Enum):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesIPCPLocalIPAddressGetValueInterfaceAlias(Enum):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesIPCPRemoteIPAddressGetValueInterfaceAlias(Enum):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesIPv6CPRemoteInterfaceIdentifierGetValueInterfaceAlias(
    Enum
):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesStatusGetValueInterfaceAlias(Enum):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesEnableGetValueInterfaceAlias(Enum):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesEnableSetValueInterfaceAlias(Enum):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesStatusSubscribeForNotificationInterfaceAlias(
    Enum
):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesUsernameGetValueInterfaceAlias(Enum):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDevicePPPInterfacesUsernameSetValueInterfaceAlias(Enum):
    PPP_DSL_DATA = auto()
    PPP_FTTH_DATA = auto()


class HomeHubActionDeviceRouterAdvertisementInterfaceSettingsAdvManagedFlagGetValueInterfaceSettingAlias(
    Enum
):
    RA_BR_LAN = auto()


class HomeHubActionDeviceRouterAdvertisementInterfaceSettingsAdvOtherConfigFlagGetValueInterfaceSettingAlias(
    Enum
):
    RA_BR_LAN = auto()


class HomeHubActionDeviceServicesVoiceServicesCallControlLinesGetValueVoiceServiceAlias(
    Enum
):
    VOICESERVICE1 = auto()


class HomeHubActionDeviceServicesVoiceServicesCallControlLinesGetValueLineAlias(Enum):
    LINE1 = auto()


class HomeHubActionDeviceServicesVoiceServicesCallLogsGetValueVoiceServiceAlias(Enum):
    VOICESERVICE1 = auto()


class HomeHubActionDeviceServicesVoiceServicesSIPClientsLastRegistrationTimeGetValueVoiceServiceAlias(
    Enum
):
    VOICESERVICE1 = auto()


class HomeHubActionDeviceServicesVoiceServicesSIPClientsLastRegistrationTimeGetValueClientAlias(
    Enum
):
    CLIENT1 = auto()


class HomeHubActionDeviceServicesVoiceServicesSIPClientsGetValueVoiceServiceAlias(Enum):
    VOICESERVICE1 = auto()


class HomeHubActionDeviceServicesVoiceServicesSIPClientsGetValueClientAlias(Enum):
    CLIENT1 = auto()


class HomeHubActionDeviceUserAccountsUsersSecretQueryGetValueUserLogin(Enum):
    admin = auto()


class HomeHubActionDeviceWiFiAccessPointsAssociatedDevicesGetValueAccessPointAlias(
    Enum
):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionDeviceWiFiAccessPointsEnableGetValueAccessPointAlias(Enum):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionDeviceWiFiAccessPointsSSIDAdvertisementEnabledGetValueAccessPointAlias(
    Enum
):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionDeviceWiFiAccessPointsSecurityKeyPassphraseGetValueAccessPointAlias(
    Enum
):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionDeviceWiFiAccessPointsSecurityModeEnabledGetValueAccessPointAlias(
    Enum
):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionDeviceWiFiAccessPointsSecurityModesSupportedGetValueAccessPointAlias(
    Enum
):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionDeviceWiFiAccessPointsSecurityWEPKeyGetValueAccessPointAlias(Enum):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionDeviceWiFiAccessPointsWPSEnableGetValueAccessPointAlias(Enum):
    PRIV0 = auto()
    PRIV1 = auto()


class HomeHubActionDeviceWiFiRadiosAutoChannelEnableGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosAutoChannelTriggerGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosChannelGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosChannelsInUseGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosEnableGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosExtensionChannelGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosMaxBitRateGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosOperatingChannelBandwidthGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosOperatingStandardsGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosPossibleChannelsGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiRadiosTransmitPowerGetValueRadioAlias(Enum):
    RADIO5G = auto()
    RADIO2G4 = auto()


class HomeHubActionDeviceWiFiSSIDsConnectionTimeGetValueSSIDAlias(Enum):
    WL_PRIV5G = auto()
    WL_PRIV2G = auto()


class HomeHubActionDeviceWiFiSSIDsEnableGetValueSSIDAlias(Enum):
    WL_PRIV5G = auto()
    WL_PRIV2G = auto()


class HomeHubActionDeviceWiFiSSIDsMACAddressGetValueSSIDAlias(Enum):
    WL_PRIV5G = auto()
    WL_PRIV2G = auto()


class HomeHubActionDeviceWiFiSSIDsSSIDGetValueSSIDAlias(Enum):
    WL_REDSIDE_X1_2G = auto()
    WL_REDSIDE_O1_5G = auto()
    WL_REDSIDE_O1_2G = auto()
    WL_REDSIDE_X1_5G = auto()
    WL_PRIV5G = auto()
    WL_PRIV2G = auto()


class HomeHubActionDeviceWiFiSSIDsStatusGetValueSSIDAlias(Enum):
    WL_PRIV5G = auto()
    WL_PRIV2G = auto()


class HomeHubActionDeviceWiFiSSIDsGetValueSSIDAlias(Enum):
    WL_PRIV5G = auto()
    WL_PRIV2G = auto()


class HomeHubActionDeviceATMLinksDestinationAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, link_alias: HomeHubActionDeviceATMLinksDestinationAddressGetValueLinkAlias
    ):
        self.link_alias = link_alias

    @property
    def xpath(self):
        return (
            f"Device/ATM/Links/Link[Alias='{self.link_alias.name}']/DestinationAddress"
        )


class HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, pool_alias: HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValuePoolAlias
    ):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Enable"


class HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        pool_alias: HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValuePoolAlias,
    ):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/IPInterface"


class HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, pool_alias: HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValuePoolAlias
    ):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return (
            f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/LeaseTime"
        )


class HomeHubActionDeviceDHCPv4ServerPoolsMaxAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        pool_alias: HomeHubActionDeviceDHCPv4ServerPoolsMaxAddressGetValuePoolAlias,
    ):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/MaxAddress"


class HomeHubActionDeviceDHCPv4ServerPoolsMinAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        pool_alias: HomeHubActionDeviceDHCPv4ServerPoolsMinAddressGetValuePoolAlias,
    ):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/MinAddress"


class HomeHubActionDeviceDHCPv4ServerPoolsStaticAddressesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        pool_alias: HomeHubActionDeviceDHCPv4ServerPoolsStaticAddressesGetValuePoolAlias,
    ):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/StaticAddresses"


class HomeHubActionDeviceDHCPv4ServerPoolsSubnetMaskGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        pool_alias: HomeHubActionDeviceDHCPv4ServerPoolsSubnetMaskGetValuePoolAlias,
    ):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/SubnetMask"


class HomeHubActionDeviceDHCPv4ServerX_SAGEMCOM_AuthoritativeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DHCPv4/Server/X_SAGEMCOM_Authoritative"


class HomeHubActionDeviceDHCPv6ServerPoolsClientsIPv6AddressesIPv6AddressIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        pool_alias: HomeHubActionDeviceDHCPv6ServerPoolsClientsIPv6AddressesIPv6AddressIPAddressGetValuePoolAlias,
        client_active: HomeHubActionDeviceDHCPv6ServerPoolsClientsIPv6AddressesIPv6AddressIPAddressGetValueClientActive,
    ):
        self.pool_alias = pool_alias
        self.client_active = client_active

    @property
    def xpath(self):
        return f"Device/DHCPv6/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Clients/Client[Active='{self.client_active.name}']/IPv6Addresses/IPv6Address/IPAddress"


class HomeHubActionDeviceDHCPv6ServerPoolsIANAEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        pool_alias: HomeHubActionDeviceDHCPv6ServerPoolsIANAEnableGetValuePoolAlias,
    ):
        self.pool_alias = pool_alias

    @property
    def xpath(self):
        return f"Device/DHCPv6/Server/Pools/Pool[Alias='{self.pool_alias.name}']/IANAEnable"


class HomeHubActionDeviceDHCPv6ServerPoolsStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, pool_alias: HomeHubActionDeviceDHCPv6ServerPoolsStatusGetValuePoolAlias
    ):
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


class HomeHubActionDeviceDNSRelayForwardingsDNSServerGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        forwarding_status: HomeHubActionDeviceDNSRelayForwardingsDNSServerGetValueForwardingStatus,
    ):
        self.forwarding_status = forwarding_status

    @property
    def xpath(self):
        return f"Device/DNS/Relay/Forwardings/Forwarding[Status='{self.forwarding_status.name}']/DNSServer"


class HomeHubActionDeviceDNSRelayLocalDomainsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/DNS/Relay/LocalDomains"


class HomeHubActionDeviceDSLChannelsDownstreamCurrRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, channel_uid: int):
        self.channel_uid = channel_uid

    @property
    def xpath(self):
        return (
            f"Device/DSL/Channels/Channel[@uid='{self.channel_uid}']/DownstreamCurrRate"
        )


class HomeHubActionDeviceDSLChannelsUpstreamCurrRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, channel_uid: int):
        self.channel_uid = channel_uid

    @property
    def xpath(self):
        return (
            f"Device/DSL/Channels/Channel[@uid='{self.channel_uid}']/UpstreamCurrRate"
        )


class HomeHubActionDeviceDSLChannelsActualInterleavingDelayGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        channel_alias: HomeHubActionDeviceDSLChannelsActualInterleavingDelayGetValueChannelAlias,
    ):
        self.channel_alias = channel_alias

    @property
    def xpath(self):
        return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/ActualInterleavingDelay"


class HomeHubActionDeviceDSLChannelsActualInterleavingDelayusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        channel_alias: HomeHubActionDeviceDSLChannelsActualInterleavingDelayusGetValueChannelAlias,
    ):
        self.channel_alias = channel_alias

    @property
    def xpath(self):
        return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/ActualInterleavingDelayus"


class HomeHubActionDeviceDSLChannelsDownstreamCurrRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        channel_alias: HomeHubActionDeviceDSLChannelsDownstreamCurrRateGetValueChannelAlias,
    ):
        self.channel_alias = channel_alias

    @property
    def xpath(self):
        return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/DownstreamCurrRate"


class HomeHubActionDeviceDSLChannelsUpstreamCurrRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        channel_alias: HomeHubActionDeviceDSLChannelsUpstreamCurrRateGetValueChannelAlias,
    ):
        self.channel_alias = channel_alias

    @property
    def xpath(self):
        return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/UpstreamCurrRate"


class HomeHubActionDeviceDSLLinesLastChangeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_uid: int):
        self.line_uid = line_uid

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/LastChange"


class HomeHubActionDeviceDSLLinesStatsBytesReceivedGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_uid: int):
        self.line_uid = line_uid

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/Stats/BytesReceived"


class HomeHubActionDeviceDSLLinesStatsBytesSentGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_uid: int):
        self.line_uid = line_uid

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/Stats/BytesSent"


class HomeHubActionDeviceDSLLinesDownstreamAttenuationGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        line_alias: HomeHubActionDeviceDSLLinesDownstreamAttenuationGetValueLineAlias,
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamAttenuation"


class HomeHubActionDeviceDSLLinesDownstreamMaxBitRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        line_alias: HomeHubActionDeviceDSLLinesDownstreamMaxBitRateGetValueLineAlias,
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamMaxBitRate"


class HomeHubActionDeviceDSLLinesDownstreamNoiseMarginGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        line_alias: HomeHubActionDeviceDSLLinesDownstreamNoiseMarginGetValueLineAlias,
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamNoiseMargin"


class HomeHubActionDeviceDSLLinesFirmwareVersionGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, line_alias: HomeHubActionDeviceDSLLinesFirmwareVersionGetValueLineAlias
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/FirmwareVersion"


class HomeHubActionDeviceDSLLinesLastChangeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, line_alias: HomeHubActionDeviceDSLLinesLastChangeGetValueLineAlias
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/LastChange"


class HomeHubActionDeviceDSLLinesSignalDownstreamAttenuationGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        line_alias: HomeHubActionDeviceDSLLinesSignalDownstreamAttenuationGetValueLineAlias,
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/SignalDownstreamAttenuation"


class HomeHubActionDeviceDSLLinesSignalUpstreamAttenuationGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        line_alias: HomeHubActionDeviceDSLLinesSignalUpstreamAttenuationGetValueLineAlias,
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/SignalUpstreamAttenuation"


class HomeHubActionDeviceDSLLinesStandardUsedGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, line_alias: HomeHubActionDeviceDSLLinesStandardUsedGetValueLineAlias
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/StandardUsed"


class HomeHubActionDeviceDSLLinesStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_alias: HomeHubActionDeviceDSLLinesStatusGetValueLineAlias):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/Status"


class HomeHubActionDeviceDSLLinesUpstreamAttenuationGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        line_alias: HomeHubActionDeviceDSLLinesUpstreamAttenuationGetValueLineAlias,
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return (
            f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/UpstreamAttenuation"
        )


class HomeHubActionDeviceDSLLinesUpstreamMaxBitRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, line_alias: HomeHubActionDeviceDSLLinesUpstreamMaxBitRateGetValueLineAlias
    ):
        self.line_alias = line_alias

    @property
    def xpath(self):
        return (
            f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/UpstreamMaxBitRate"
        )


class HomeHubActionDeviceDSLLinesUpstreamNoiseMarginGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        line_alias: HomeHubActionDeviceDSLLinesUpstreamNoiseMarginGetValueLineAlias,
    ):
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


class HomeHubActionDeviceDeviceInfoVendorLogFilesGetVendorLogDownloadURI(
    HomeHubAction, MethodGetVendorLogDownloadURIMixin
):
    def __init__(self, vendorlogfile_uid: int):
        self.vendorlogfile_uid = vendorlogfile_uid

    @property
    def xpath(self):
        return f"Device/DeviceInfo/VendorLogFiles/VendorLogFile[@uid='{self.vendorlogfile_uid}']"

    parameters = {"FileName": "eventLog"}


class HomeHubActionDeviceEthernetInterfacesStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceEthernetInterfacesStatusGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/Ethernet/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


class HomeHubActionDeviceEthernetInterfacesMACAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceEthernetInterfacesMACAddressGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/Ethernet/Interfaces/Interface[Alias='{self.interface_alias.name}']/MACAddress"


class HomeHubActionDeviceEthernetLinksLowerLayersGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, link_alias: HomeHubActionDeviceEthernetLinksLowerLayersGetValueLinkAlias
    ):
        self.link_alias = link_alias

    @property
    def xpath(self):
        return f"Device/Ethernet/Links/Link[Alias='{self.link_alias.name}']/LowerLayers"


class HomeHubActionDeviceEthernetVLANTerminationsVLANIDGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        vlantermination_alias: HomeHubActionDeviceEthernetVLANTerminationsVLANIDGetValueVLANTerminationAlias,
    ):
        self.vlantermination_alias = vlantermination_alias

    @property
    def xpath(self):
        return f"Device/Ethernet/VLANTerminations/VLANTermination[Alias='{self.vlantermination_alias.name}']/VLANID"


class HomeHubActionDeviceFASTLinesStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, line_uid: int):
        self.line_uid = line_uid

    @property
    def xpath(self):
        return f"Device/FAST/Lines/Line[@uid='{self.line_uid}']/Status"


class HomeHubActionDeviceFirewallChainsRulesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, chain_name: HomeHubActionDeviceFirewallChainsRulesGetValueChainName
    ):
        self.chain_name = chain_name

    @property
    def xpath(self):
        return f"Device/Firewall/Chains/Chain[Name='{self.chain_name.name}']/Rules"


class HomeHubActionDeviceFirewallChainsRulesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        chain_name: HomeHubActionDeviceFirewallChainsRulesGetValueChainName,
        rule_ipversion: int,
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


class HomeHubActionDeviceFirewallLevelsDefaultPolicyGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        level_name: HomeHubActionDeviceFirewallLevelsDefaultPolicyGetValueLevelName,
    ):
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


class HomeHubActionDeviceHostsHostsGetValue(
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


class HomeHubActionDeviceIPInterfacesIPv6AddressesIPv6AddressIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv6AddressesIPv6AddressIPAddressGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address/IPAddress"


class HomeHubActionDeviceIPInterfacesIPv6AddressesIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv6AddressesIPAddressGetValueInterfaceAlias,
        ipv6address_alias: HomeHubActionDeviceIPInterfacesIPv6AddressesIPAddressGetValueIPv6AddressAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv6address_alias = ipv6address_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address[Alias='{self.ipv6address_alias.name}']/IPAddress"


class HomeHubActionDeviceIPInterfacesIPv6AddressesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv6AddressesGetValueInterfaceAlias,
        ipv6address_ipaddressstatus: HomeHubActionDeviceIPInterfacesIPv6AddressesGetValueIPv6AddressIPAddressStatus,
    ):
        self.interface_alias = interface_alias
        self.ipv6address_ipaddressstatus = ipv6address_ipaddressstatus

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address[IPAddressStatus='{self.ipv6address_ipaddressstatus.name}']"


class HomeHubActionDeviceIPInterfacesIPv6PrefixesPrefixGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv6PrefixesPrefixGetValueInterfaceAlias,
        ipv6prefix_alias: HomeHubActionDeviceIPInterfacesIPv6PrefixesPrefixGetValueIPv6PrefixAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv6prefix_alias = ipv6prefix_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Prefixes/IPv6Prefix[Alias='{self.ipv6prefix_alias.name}']/Prefix"


class HomeHubActionDeviceIPInterfacesIPv6PrefixesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv6PrefixesGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Prefixes"


class HomeHubActionDeviceIPInterfacesULAEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesULAEnableGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/ULAEnable"


class HomeHubActionDeviceIPInterfacesIPv4AddressesIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv4AddressesIPAddressGetValueInterfaceAlias,
        ipv4address_alias: HomeHubActionDeviceIPInterfacesIPv4AddressesIPAddressGetValueIPv4AddressAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv4address_alias = ipv4address_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/IPAddress"


class HomeHubActionDeviceIPInterfacesIPv4AddressesSubnetMaskGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv4AddressesSubnetMaskGetValueInterfaceAlias,
        ipv4address_alias: HomeHubActionDeviceIPInterfacesIPv4AddressesSubnetMaskGetValueIPv4AddressAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv4address_alias = ipv4address_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/SubnetMask"


class HomeHubActionDeviceIPInterfacesIPv4AddressesIPv4AddressIPGatewayGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv4AddressesIPv4AddressIPGatewayGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address/IPGateway"


class HomeHubActionDeviceIPInterfacesIPv4AddressesDnsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesIPv4AddressesDnsGetValueInterfaceAlias,
        ipv4address_alias: HomeHubActionDeviceIPInterfacesIPv4AddressesDnsGetValueIPv4AddressAlias,
    ):
        self.interface_alias = interface_alias
        self.ipv4address_alias = ipv4address_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/Dns"


class HomeHubActionDeviceIPInterfacesLastChangeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesLastChangeGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/LastChange"


class HomeHubActionDeviceIPInterfacesStatsBytesReceivedGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesStatsBytesReceivedGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Stats/BytesReceived"


class HomeHubActionDeviceIPInterfacesStatsBytesSentGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesStatsBytesSentGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Stats/BytesSent"


class HomeHubActionDeviceIPInterfacesStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesStatusGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


class HomeHubActionDeviceIPInterfacesStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDeviceIPInterfacesStatusSubscribeForNotificationInterfaceAlias,
        id: int,
    ):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    parameters = {"id": "2", "type": "value-change", "current-value": False}


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

    parameters = {"value": 0}


class HomeHubActionDeviceManagersHubLightControlBrightnessSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/HubLightControl/Brightness"

    parameters = {"value": 100}


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

    parameters = {"value": "OFF"}


class HomeHubActionDeviceManagersHubLightControlLedEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/HubLightControl/LedEnable"

    parameters = {"value": "ON"}


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

    parameters = {"value": False}


class HomeHubActionDeviceManagersHubLightControlScheduleEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Managers/HubLightControl/Schedule/Enable"

    parameters = {"value": True}


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

    parameters = {"value": 3540}


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

    parameters = {"value": 3360}


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

    parameters = {"value": ""}


class HomeHubActionDeviceNATPortMappingsInternalClientGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        portmapping_alias: HomeHubActionDeviceNATPortMappingsInternalClientGetValuePortMappingAlias,
    ):
        self.portmapping_alias = portmapping_alias

    @property
    def xpath(self):
        return f"Device/NAT/PortMappings/PortMapping[Alias='{self.portmapping_alias.name}']/InternalClient"


class HomeHubActionDeviceNATPortMappingsInternalMACAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        portmapping_alias: HomeHubActionDeviceNATPortMappingsInternalMACAddressGetValuePortMappingAlias,
    ):
        self.portmapping_alias = portmapping_alias

    @property
    def xpath(self):
        return f"Device/NAT/PortMappings/PortMapping[Alias='{self.portmapping_alias.name}']/InternalMACAddress"


class HomeHubActionDeviceNATPortMappingsEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        portmapping_service: HomeHubActionDeviceNATPortMappingsEnableGetValuePortMappingService,
    ):
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


class HomeHubActionDevicePPPInterfacesConnectionStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesConnectionStatusGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/ConnectionStatus"


class HomeHubActionDevicePPPInterfacesIPCPLocalIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesIPCPLocalIPAddressGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPCP/LocalIPAddress"


class HomeHubActionDevicePPPInterfacesIPCPRemoteIPAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesIPCPRemoteIPAddressGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPCP/RemoteIPAddress"


class HomeHubActionDevicePPPInterfacesIPv6CPRemoteInterfaceIdentifierGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesIPv6CPRemoteInterfaceIdentifierGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6CP/RemoteInterfaceIdentifier"


class HomeHubActionDevicePPPInterfacesStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesStatusGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


class HomeHubActionDevicePPPInterfacesEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesEnableGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Enable"


class HomeHubActionDevicePPPInterfacesEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesEnableSetValueInterfaceAlias,
        value: any,
    ):
        self.interface_alias = interface_alias
        self.value = value

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Enable"

    parameters = {"value": False}


class HomeHubActionDevicePPPInterfacesEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesEnableSetValueInterfaceAlias,
        value: any,
    ):
        self.interface_alias = interface_alias
        self.value = value

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Enable"

    parameters = {"value": True}


class HomeHubActionDevicePPPInterfacesStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesStatusSubscribeForNotificationInterfaceAlias,
        id: int,
    ):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    parameters = {"id": "1", "type": "value-change", "current-value": False}


class HomeHubActionDevicePPPInterfacesStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesStatusSubscribeForNotificationInterfaceAlias,
        id: int,
    ):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    parameters = {"id": "2", "type": "value-change", "current-value": False}


class HomeHubActionDevicePPPInterfacesStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesStatusSubscribeForNotificationInterfaceAlias,
        id: int,
    ):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    parameters = {"id": "4", "type": "value-change", "current-value": False}


class HomeHubActionDevicePPPInterfacesStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesStatusSubscribeForNotificationInterfaceAlias,
        id: int,
    ):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    parameters = {"id": "6", "type": "value-change", "current-value": False}


class HomeHubActionDevicePPPInterfacesUsernameGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesUsernameGetValueInterfaceAlias,
    ):
        self.interface_alias = interface_alias

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Username"


class HomeHubActionDevicePPPInterfacesUsernameSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesUsernameSetValueInterfaceAlias,
        value: any,
    ):
        self.interface_alias = interface_alias
        self.value = value

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Username"

    parameters = {"value": "bthomehub@btbroadband.com"}


class HomeHubActionDevicePPPInterfacesStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesStatusSubscribeForNotificationInterfaceAlias,
        id: int,
    ):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    parameters = {"id": "3", "type": "value-change", "current-value": False}


class HomeHubActionDevicePPPInterfacesStatusSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(
        self,
        interface_alias: HomeHubActionDevicePPPInterfacesStatusSubscribeForNotificationInterfaceAlias,
        id: int,
    ):
        self.interface_alias = interface_alias
        self.id = id

    @property
    def xpath(self):
        return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

    parameters = {"id": "5", "type": "value-change", "current-value": False}


class HomeHubActionDeviceRouterAdvertisementInterfaceSettingsAdvManagedFlagGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interfacesetting_alias: HomeHubActionDeviceRouterAdvertisementInterfaceSettingsAdvManagedFlagGetValueInterfaceSettingAlias,
    ):
        self.interfacesetting_alias = interfacesetting_alias

    @property
    def xpath(self):
        return f"Device/RouterAdvertisement/InterfaceSettings/InterfaceSetting[Alias='{self.interfacesetting_alias.name}']/AdvManagedFlag"


class HomeHubActionDeviceRouterAdvertisementInterfaceSettingsAdvOtherConfigFlagGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        interfacesetting_alias: HomeHubActionDeviceRouterAdvertisementInterfaceSettingsAdvOtherConfigFlagGetValueInterfaceSettingAlias,
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

    parameters = {"value": False}


class HomeHubActionDeviceServicesDeviceConfigPortClampingEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, value: any):
        self.value = value

    xpath = "Device/Services/DeviceConfig/PortClampingEnable"

    parameters = {"value": True}


class HomeHubActionDeviceServicesDeviceConfigWiFiModeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/WiFiMode"


class HomeHubActionDeviceServicesDeviceConfigWifiPasswordForbiddenWordsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    xpath = "Device/Services/DeviceConfig/WifiPasswordForbiddenWords"


class HomeHubActionDeviceServicesDynamicDNSClientsEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Enable"

    parameters = {"value": False}


class HomeHubActionDeviceServicesDynamicDNSClientsEnableSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Enable"

    parameters = {"value": True}


class HomeHubActionDeviceServicesDynamicDNSClientsHostnamesNameSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, hostname_uid: int, value: any):
        self.client_uid = client_uid
        self.hostname_uid = hostname_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Hostnames/Hostname[@uid='{self.hostname_uid}']/Name"

    parameters = {"value": "http://atestdomain.duckdns.org/"}


class HomeHubActionDeviceServicesDynamicDNSClientsPasswordSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Password"

    parameters = {"value": "f3fd60b2-88d9-4c20-a55a-260ca6e8daac"}


class HomeHubActionDeviceServicesDynamicDNSClientsServiceReferenceSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/ServiceReference"

    parameters = {"value": 'Device/Services/DynamicDNS/Services/Service[@uid="2"]'}


class HomeHubActionDeviceServicesDynamicDNSClientsUsernameSetValue(
    HomeHubAction, MethodSetValueMixin
):
    def __init__(self, client_uid: int, value: any):
        self.client_uid = client_uid
        self.value = value

    @property
    def xpath(self):
        return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Username"

    parameters = {"value": "christopher.hampson58@gmail.com"}


class HomeHubActionDeviceServicesDynamicDNSClientsGetValue(
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


class HomeHubActionDeviceServicesStorageServicesLogicalVolumesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, storageservice_uid: int):
        self.storageservice_uid = storageservice_uid

    @property
    def xpath(self):
        return f"Device/Services/StorageServices/StorageService[@uid='{self.storageservice_uid}']/LogicalVolumes"


class HomeHubActionDeviceServicesVoiceServicesCallControlLinesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        voiceservice_alias: HomeHubActionDeviceServicesVoiceServicesCallControlLinesGetValueVoiceServiceAlias,
        line_alias: HomeHubActionDeviceServicesVoiceServicesCallControlLinesGetValueLineAlias,
    ):
        self.voiceservice_alias = voiceservice_alias
        self.line_alias = line_alias

    @property
    def xpath(self):
        return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/CallControl/Lines/Line[Alias='{self.line_alias.name}']"


class HomeHubActionDeviceServicesVoiceServicesCallLogsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        voiceservice_alias: HomeHubActionDeviceServicesVoiceServicesCallLogsGetValueVoiceServiceAlias,
    ):
        self.voiceservice_alias = voiceservice_alias

    @property
    def xpath(self):
        return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/CallLogs"


class HomeHubActionDeviceServicesVoiceServicesSIPClientsLastRegistrationTimeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        voiceservice_alias: HomeHubActionDeviceServicesVoiceServicesSIPClientsLastRegistrationTimeGetValueVoiceServiceAlias,
        client_alias: HomeHubActionDeviceServicesVoiceServicesSIPClientsLastRegistrationTimeGetValueClientAlias,
    ):
        self.voiceservice_alias = voiceservice_alias
        self.client_alias = client_alias

    @property
    def xpath(self):
        return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/SIP/Clients/Client[Alias='{self.client_alias.name}']/LastRegistrationTime"


class HomeHubActionDeviceServicesVoiceServicesSIPClientsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        voiceservice_alias: HomeHubActionDeviceServicesVoiceServicesSIPClientsGetValueVoiceServiceAlias,
        client_alias: HomeHubActionDeviceServicesVoiceServicesSIPClientsGetValueClientAlias,
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


class HomeHubActionDeviceUserAccountsUsersSecretQueryGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        user_login: HomeHubActionDeviceUserAccountsUsersSecretQueryGetValueUserLogin,
    ):
        self.user_login = user_login

    @property
    def xpath(self):
        return f"Device/UserAccounts/Users/User[Login='{self.user_login.name}']/SecretQuery"


class HomeHubActionDeviceWiFiAccessPointsAssociatedDevicesGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        accesspoint_alias: HomeHubActionDeviceWiFiAccessPointsAssociatedDevicesGetValueAccessPointAlias,
    ):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/AssociatedDevices"


class HomeHubActionDeviceWiFiAccessPointsEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        accesspoint_alias: HomeHubActionDeviceWiFiAccessPointsEnableGetValueAccessPointAlias,
    ):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Enable"


class HomeHubActionDeviceWiFiAccessPointsSSIDAdvertisementEnabledGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        accesspoint_alias: HomeHubActionDeviceWiFiAccessPointsSSIDAdvertisementEnabledGetValueAccessPointAlias,
    ):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/SSIDAdvertisementEnabled"


class HomeHubActionDeviceWiFiAccessPointsSecurityKeyPassphraseGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        accesspoint_alias: HomeHubActionDeviceWiFiAccessPointsSecurityKeyPassphraseGetValueAccessPointAlias,
    ):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/KeyPassphrase"


class HomeHubActionDeviceWiFiAccessPointsSecurityModeEnabledGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        accesspoint_alias: HomeHubActionDeviceWiFiAccessPointsSecurityModeEnabledGetValueAccessPointAlias,
    ):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/ModeEnabled"


class HomeHubActionDeviceWiFiAccessPointsSecurityModesSupportedGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        accesspoint_alias: HomeHubActionDeviceWiFiAccessPointsSecurityModesSupportedGetValueAccessPointAlias,
    ):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/ModesSupported"


class HomeHubActionDeviceWiFiAccessPointsSecurityWEPKeyGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        accesspoint_alias: HomeHubActionDeviceWiFiAccessPointsSecurityWEPKeyGetValueAccessPointAlias,
    ):
        self.accesspoint_alias = accesspoint_alias

    @property
    def xpath(self):
        return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/WEPKey"


class HomeHubActionDeviceWiFiAccessPointsWPSEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        accesspoint_alias: HomeHubActionDeviceWiFiAccessPointsWPSEnableGetValueAccessPointAlias,
    ):
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

    parameters = {"id": "1", "type": "value-change", "current-value": False}


class HomeHubActionDeviceWiFiRadiosRadioChannelSubscribeForNotification(
    HomeHubAction, MethodSubscribeForNotificationMixin
):
    def __init__(self, id: int):
        self.id = id

    xpath = "Device/WiFi/Radios/Radio/Channel"

    parameters = {"id": "3", "type": "value-change", "current-value": False}


class HomeHubActionDeviceWiFiRadiosAutoChannelEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        radio_alias: HomeHubActionDeviceWiFiRadiosAutoChannelEnableGetValueRadioAlias,
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/AutoChannelEnable"


class HomeHubActionDeviceWiFiRadiosAutoChannelTriggerGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        radio_alias: HomeHubActionDeviceWiFiRadiosAutoChannelTriggerGetValueRadioAlias,
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/AutoChannelTrigger"


class HomeHubActionDeviceWiFiRadiosChannelGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, radio_alias: HomeHubActionDeviceWiFiRadiosChannelGetValueRadioAlias
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/Channel"


class HomeHubActionDeviceWiFiRadiosChannelsInUseGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, radio_alias: HomeHubActionDeviceWiFiRadiosChannelsInUseGetValueRadioAlias
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return (
            f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/ChannelsInUse"
        )


class HomeHubActionDeviceWiFiRadiosEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, radio_alias: HomeHubActionDeviceWiFiRadiosEnableGetValueRadioAlias
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/Enable"


class HomeHubActionDeviceWiFiRadiosExtensionChannelGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        radio_alias: HomeHubActionDeviceWiFiRadiosExtensionChannelGetValueRadioAlias,
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/ExtensionChannel"


class HomeHubActionDeviceWiFiRadiosMaxBitRateGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, radio_alias: HomeHubActionDeviceWiFiRadiosMaxBitRateGetValueRadioAlias
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/MaxBitRate"


class HomeHubActionDeviceWiFiRadiosOperatingChannelBandwidthGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        radio_alias: HomeHubActionDeviceWiFiRadiosOperatingChannelBandwidthGetValueRadioAlias,
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/OperatingChannelBandwidth"


class HomeHubActionDeviceWiFiRadiosOperatingStandardsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        radio_alias: HomeHubActionDeviceWiFiRadiosOperatingStandardsGetValueRadioAlias,
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/OperatingStandards"


class HomeHubActionDeviceWiFiRadiosPossibleChannelsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self,
        radio_alias: HomeHubActionDeviceWiFiRadiosPossibleChannelsGetValueRadioAlias,
    ):
        self.radio_alias = radio_alias

    @property
    def xpath(self):
        return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/PossibleChannels"


class HomeHubActionDeviceWiFiRadiosTransmitPowerGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, radio_alias: HomeHubActionDeviceWiFiRadiosTransmitPowerGetValueRadioAlias
    ):
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


class HomeHubActionDeviceWiFiSSIDsConnectionTimeGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, ssid_alias: HomeHubActionDeviceWiFiSSIDsConnectionTimeGetValueSSIDAlias
    ):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/ConnectionTime"


class HomeHubActionDeviceWiFiSSIDsEnableGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionDeviceWiFiSSIDsEnableGetValueSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/Enable"


class HomeHubActionDeviceWiFiSSIDsMACAddressGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(
        self, ssid_alias: HomeHubActionDeviceWiFiSSIDsMACAddressGetValueSSIDAlias
    ):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/MACAddress"


class HomeHubActionDeviceWiFiSSIDsSSIDGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionDeviceWiFiSSIDsSSIDGetValueSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/SSID"


class HomeHubActionDeviceWiFiSSIDsStatusGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionDeviceWiFiSSIDsStatusGetValueSSIDAlias):
        self.ssid_alias = ssid_alias

    @property
    def xpath(self):
        return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/Status"


class HomeHubActionDeviceWiFiSSIDsGetValue(
    HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
):
    def __init__(self, ssid_alias: HomeHubActionDeviceWiFiSSIDsGetValueSSIDAlias):
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

    parameters = {
        "user": "admin",
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


class HomeHubActionLogIn(HomeHubAction, MethodLogInMixin):
    def __init__(self, user: str):
        self.user = user

    parameters = {
        "user": "guest",
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

    parameters = {"id": "1"}


class HomeHubActionUnsubscribeForNotification(
    HomeHubAction, MethodUnsubscribeForNotificationMixin
):
    def __init__(self, id: int):
        self.id = id

    parameters = {"id": "2"}


class HomeHubActionUnsubscribeForNotification(
    HomeHubAction, MethodUnsubscribeForNotificationMixin
):
    def __init__(self, id: int):
        self.id = id

    parameters = {"id": "3"}


class HomeHubActionUnsubscribeForNotification(
    HomeHubAction, MethodUnsubscribeForNotificationMixin
):
    def __init__(self, id: int):
        self.id = id

    parameters = {"id": "4"}


class HomeHubActionUnsubscribeForNotification(
    HomeHubAction, MethodUnsubscribeForNotificationMixin
):
    def __init__(self, id: int):
        self.id = id

    parameters = {"id": "5"}
