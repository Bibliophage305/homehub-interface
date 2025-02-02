from homehub_interface.homehubsession import HomeHubSession

from homehub_interface.homehubaction import *


# class HomeHubActionDeviceATMLinksDestinationAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, link_alias: HomeHubActionXPathParamLinkAlias):
#         self.link_alias = link_alias

#     @property
#     def xpath(self):
#         return (
#             f"Device/ATM/Links/Link[Alias='{self.link_alias.name}']/DestinationAddress"
#         )


def test_HomeHubActionDeviceATMLinksDestinationAddressGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceATMLinksDestinationAddressGetValue(link_alias)
        for link_alias in HomeHubActionXPathParamLinkAlias
    ]
    assert session.make_request(actions).response


# class HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Enable"


def test_HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request(actions).response


# class HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/IPInterface"


def test_HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request(actions).response


# class HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return (
#             f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/LeaseTime"
#         )


def test_HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request(actions).response


# class HomeHubActionDeviceDHCPv4ServerPoolsMaxAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/MaxAddress"

def test_HomeHubActionDeviceDHCPv4ServerPoolsMaxAddressGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsMaxAddressGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request(actions).response

# class HomeHubActionDeviceDHCPv4ServerPoolsMinAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/MinAddress"
# class HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Enable"


def test_HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsEnableGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request(actions).response


# class HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/IPInterface"


def test_HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsIPInterfaceGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request(actions).response


# class HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return (
#             f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/LeaseTime"
#         )


def test_HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsLeaseTimeGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request(actions).response

# class HomeHubActionDeviceDHCPv4ServerPoolsStaticAddressesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/StaticAddresses"

def test_HomeHubActionDeviceDHCPv4ServerPoolsStaticAddressesGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsStaticAddressesGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request(actions).response

# class HomeHubActionDeviceDHCPv4ServerPoolsSubnetMaskGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv4/Server/Pools/Pool[Alias='{self.pool_alias.name}']/SubnetMask"

def test_HomeHubActionDeviceDHCPv4ServerPoolsSubnetMaskGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerPoolsSubnetMaskGetValue(pool_alias)
        for pool_alias in HomeHubActionXPathParamPoolAlias
    ]
    assert session.make_request

# class HomeHubActionDeviceDHCPv4ServerX_SAGEMCOM_AuthoritativeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DHCPv4/Server/X_SAGEMCOM_Authoritative"

def test_HomeHubActionDeviceDHCPv4ServerX_SAGEMCOM_AuthoritativeGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv4ServerX_SAGEMCOM_AuthoritativeGetValue()
    ]
    assert session.make_request(actions).response

# class HomeHubActionDeviceDHCPv6ServerPoolsClientsIPv6AddressesIPv6AddressIPAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         pool_alias: HomeHubActionXPathParamPoolAlias,
#         client_active: HomeHubActionXPathParamClientActive,
#     ):
#         self.pool_alias = pool_alias
#         self.client_active = client_active

def test_HomeHubActionDeviceDHCPv6ServerPoolsClientsIPv6AddressesIPv6AddressIPAddressGetValue():
    session = HomeHubSession(timeout=1)
    session.authenticate_admin()
    actions = [
        HomeHubActionDeviceDHCPv6ServerPoolsClientsIPv6AddressesIPv6AddressIPAddressGetValue(pool_alias, client_active)
        for pool_alias in HomeHubActionXPathParamPoolAlias
        for client_active in HomeHubActionXPathParamClientActive
    ]
    assert session.make_request(actions).response

#     @property
#     def xpath(self):
#         return f"Device/DHCPv6/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Clients/Client[Active='{self.client_active.name}']/IPv6Addresses/IPv6Address/IPAddress"


# class HomeHubActionDeviceDHCPv6ServerPoolsIANAEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv6/Server/Pools/Pool[Alias='{self.pool_alias.name}']/IANAEnable"


# class HomeHubActionDeviceDHCPv6ServerPoolsStatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, pool_alias: HomeHubActionXPathParamPoolAlias):
#         self.pool_alias = pool_alias

#     @property
#     def xpath(self):
#         return f"Device/DHCPv6/Server/Pools/Pool[Alias='{self.pool_alias.name}']/Status"


# class HomeHubActionDeviceDNSClientHostNameGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DNS/Client/HostName"


# class HomeHubActionDeviceDNSClientLocalDomainsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DNS/Client/LocalDomains"


# class HomeHubActionDeviceDNSRelayForwardingsDNSServerGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, forwarding_status: HomeHubActionXPathParamForwardingStatus):
#         self.forwarding_status = forwarding_status

#     @property
#     def xpath(self):
#         return f"Device/DNS/Relay/Forwardings/Forwarding[Status='{self.forwarding_status.name}']/DNSServer"


# class HomeHubActionDeviceDNSRelayLocalDomainsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DNS/Relay/LocalDomains"


# class HomeHubActionDeviceDSLChannelsDownstreamCurrRateGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, channel_uid: int):
#         self.channel_uid = channel_uid

#     @property
#     def xpath(self):
#         return (
#             f"Device/DSL/Channels/Channel[@uid='{self.channel_uid}']/DownstreamCurrRate"
#         )


# class HomeHubActionDeviceDSLChannelsUpstreamCurrRateGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, channel_uid: int):
#         self.channel_uid = channel_uid

#     @property
#     def xpath(self):
#         return (
#             f"Device/DSL/Channels/Channel[@uid='{self.channel_uid}']/UpstreamCurrRate"
#         )


# class HomeHubActionDeviceDSLChannelsActualInterleavingDelayGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, channel_alias: HomeHubActionXPathParamChannelAlias):
#         self.channel_alias = channel_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/ActualInterleavingDelay"


# class HomeHubActionDeviceDSLChannelsActualInterleavingDelayusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, channel_alias: HomeHubActionXPathParamChannelAlias):
#         self.channel_alias = channel_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/ActualInterleavingDelayus"


# class HomeHubActionDeviceDSLChannelsDownstreamCurrRateGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, channel_alias: HomeHubActionXPathParamChannelAlias):
#         self.channel_alias = channel_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/DownstreamCurrRate"


# class HomeHubActionDeviceDSLChannelsUpstreamCurrRateGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, channel_alias: HomeHubActionXPathParamChannelAlias):
#         self.channel_alias = channel_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Channels/Channel[Alias='{self.channel_alias.name}']/UpstreamCurrRate"


# class HomeHubActionDeviceDSLLinesLastChangeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_uid: int):
#         self.line_uid = line_uid

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/LastChange"


# class HomeHubActionDeviceDSLLinesStatsBytesReceivedGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_uid: int):
#         self.line_uid = line_uid

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/Stats/BytesReceived"


# class HomeHubActionDeviceDSLLinesStatsBytesSentGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_uid: int):
#         self.line_uid = line_uid

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[@uid='{self.line_uid}']/Stats/BytesSent"


# class HomeHubActionDeviceDSLLinesDownstreamAttenuationGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamAttenuation"


# class HomeHubActionDeviceDSLLinesDownstreamMaxBitRateGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamMaxBitRate"


# class HomeHubActionDeviceDSLLinesDownstreamNoiseMarginGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/DownstreamNoiseMargin"


# class HomeHubActionDeviceDSLLinesFirmwareVersionGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/FirmwareVersion"


# class HomeHubActionDeviceDSLLinesLastChangeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/LastChange"


# class HomeHubActionDeviceDSLLinesSignalDownstreamAttenuationGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/SignalDownstreamAttenuation"


# class HomeHubActionDeviceDSLLinesSignalUpstreamAttenuationGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/SignalUpstreamAttenuation"


# class HomeHubActionDeviceDSLLinesStandardUsedGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/StandardUsed"


# class HomeHubActionDeviceDSLLinesStatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/Status"


# class HomeHubActionDeviceDSLLinesUpstreamAttenuationGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return (
#             f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/UpstreamAttenuation"
#         )


# class HomeHubActionDeviceDSLLinesUpstreamMaxBitRateGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return (
#             f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/UpstreamMaxBitRate"
#         )


# class HomeHubActionDeviceDSLLinesUpstreamNoiseMarginGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_alias: HomeHubActionXPathParamLineAlias):
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return (
#             f"Device/DSL/Lines/Line[Alias='{self.line_alias.name}']/UpstreamNoiseMargin"
#         )


# class HomeHubActionDeviceDeviceDiscoveryDeviceIdentificationDeviceTypesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceDiscovery/DeviceIdentification/DeviceTypes"


# class HomeHubActionDeviceDeviceInfoBootloaderVersionGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/BootloaderVersion"


# class HomeHubActionDeviceDeviceInfoExternalFirmwareVersionGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/ExternalFirmwareVersion"


# class HomeHubActionDeviceDeviceInfoHardwareVersionGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/HardwareVersion"


# class HomeHubActionDeviceDeviceInfoMACAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/MACAddress"


# class HomeHubActionDeviceDeviceInfoModelNameGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/ModelName"


# class HomeHubActionDeviceDeviceInfoProductClassGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/ProductClass"


# class HomeHubActionDeviceDeviceInfoProductVariantGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/ProductVariant"


# class HomeHubActionDeviceDeviceInfoSerialNumberGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/SerialNumber"


# class HomeHubActionDeviceDeviceInfoSupportedDataModelsSupportedDataModelURLGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/SupportedDataModels/SupportedDataModel/URL"


# class HomeHubActionDeviceDeviceInfoUpTimeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/DeviceInfo/UpTime"


# class HomeHubActionDeviceDeviceInfoVendorLogFilesGetVendorLogDownloadURI(
#     HomeHubAction, MethodGetVendorLogDownloadURIMixin
# ):
#     def __init__(self, vendorlogfile_uid: int):
#         self.vendorlogfile_uid = vendorlogfile_uid

#     @property
#     def xpath(self):
#         return f"Device/DeviceInfo/VendorLogFiles/VendorLogFile[@uid='{self.vendorlogfile_uid}']"

#     parameters = {"FileName": "eventLog"}


# class HomeHubActionDeviceEthernetInterfacesStatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/Ethernet/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


# class HomeHubActionDeviceEthernetInterfacesMACAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/Ethernet/Interfaces/Interface[Alias='{self.interface_alias.name}']/MACAddress"


# class HomeHubActionDeviceEthernetLinksLowerLayersGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, link_alias: HomeHubActionXPathParamLinkAlias):
#         self.link_alias = link_alias

#     @property
#     def xpath(self):
#         return f"Device/Ethernet/Links/Link[Alias='{self.link_alias.name}']/LowerLayers"


# class HomeHubActionDeviceEthernetVLANTerminationsVLANIDGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self, vlantermination_alias: HomeHubActionXPathParamVLANTerminationAlias
#     ):
#         self.vlantermination_alias = vlantermination_alias

#     @property
#     def xpath(self):
#         return f"Device/Ethernet/VLANTerminations/VLANTermination[Alias='{self.vlantermination_alias.name}']/VLANID"


# class HomeHubActionDeviceFASTLinesStatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, line_uid: int):
#         self.line_uid = line_uid

#     @property
#     def xpath(self):
#         return f"Device/FAST/Lines/Line[@uid='{self.line_uid}']/Status"


# class HomeHubActionDeviceFirewallChainsRulesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, chain_name: HomeHubActionXPathParamChainName):
#         self.chain_name = chain_name

#     @property
#     def xpath(self):
#         return f"Device/Firewall/Chains/Chain[Name='{self.chain_name.name}']/Rules"


# class HomeHubActionDeviceFirewallChainsRulesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self, chain_name: HomeHubActionXPathParamChainName, rule_ipversion: int
#     ):
#         self.chain_name = chain_name
#         self.rule_ipversion = rule_ipversion

#     @property
#     def xpath(self):
#         return f"Device/Firewall/Chains/Chain[Name='{self.chain_name.name}']/Rules/Rule[IPVersion='{self.rule_ipversion}']"


# class HomeHubActionDeviceFirewallConfigGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Firewall/Config"


# class HomeHubActionDeviceFirewallEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Firewall/Enable"


# class HomeHubActionDeviceFirewallLevelsDefaultPolicyGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, level_name: HomeHubActionXPathParamLevelName):
#         self.level_name = level_name

#     @property
#     def xpath(self):
#         return (
#             f"Device/Firewall/Levels/Level[Name='{self.level_name.name}']/DefaultPolicy"
#         )


# class HomeHubActionDeviceFirewallRespondToPingGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Firewall/RespondToPing"


# class HomeHubActionDeviceHostsHistoryMaxAgeInDaysGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Hosts/HistoryMaxAgeInDays"


# class HomeHubActionDeviceHostsHostsHostBlacklistedScheduleGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Hosts/Hosts/Host/BlacklistedSchedule"


# class HomeHubActionDeviceHostsHostsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, host_uid: int):
#         self.host_uid = host_uid

#     @property
#     def xpath(self):
#         return f"Device/Hosts/Hosts/Host[@uid='{self.host_uid}']"


# class HomeHubActionDeviceHostsHostsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Hosts/Hosts"


# class HomeHubActionDeviceIPIPv6StatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/IP/IPv6Status"


# class HomeHubActionDeviceIPInterfacesIPv6AddressesIPv6AddressIPAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address/IPAddress"


# class HomeHubActionDeviceIPInterfacesIPv6AddressesIPAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         interface_alias: HomeHubActionXPathParamInterfaceAlias,
#         ipv6address_alias: HomeHubActionXPathParamIPv6AddressAlias,
#     ):
#         self.interface_alias = interface_alias
#         self.ipv6address_alias = ipv6address_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address[Alias='{self.ipv6address_alias.name}']/IPAddress"


# class HomeHubActionDeviceIPInterfacesIPv6AddressesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         interface_alias: HomeHubActionXPathParamInterfaceAlias,
#         ipv6address_ipaddressstatus: HomeHubActionXPathParamIPv6AddressIPAddressStatus,
#     ):
#         self.interface_alias = interface_alias
#         self.ipv6address_ipaddressstatus = ipv6address_ipaddressstatus

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Addresses/IPv6Address[IPAddressStatus='{self.ipv6address_ipaddressstatus.name}']"


# class HomeHubActionDeviceIPInterfacesIPv6PrefixesPrefixGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         interface_alias: HomeHubActionXPathParamInterfaceAlias,
#         ipv6prefix_alias: HomeHubActionXPathParamIPv6PrefixAlias,
#     ):
#         self.interface_alias = interface_alias
#         self.ipv6prefix_alias = ipv6prefix_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Prefixes/IPv6Prefix[Alias='{self.ipv6prefix_alias.name}']/Prefix"


# class HomeHubActionDeviceIPInterfacesIPv6PrefixesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6Prefixes"


# class HomeHubActionDeviceIPInterfacesULAEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/ULAEnable"


# class HomeHubActionDeviceIPInterfacesIPv4AddressesIPAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         interface_alias: HomeHubActionXPathParamInterfaceAlias,
#         ipv4address_alias: HomeHubActionXPathParamIPv4AddressAlias,
#     ):
#         self.interface_alias = interface_alias
#         self.ipv4address_alias = ipv4address_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/IPAddress"


# class HomeHubActionDeviceIPInterfacesIPv4AddressesSubnetMaskGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         interface_alias: HomeHubActionXPathParamInterfaceAlias,
#         ipv4address_alias: HomeHubActionXPathParamIPv4AddressAlias,
#     ):
#         self.interface_alias = interface_alias
#         self.ipv4address_alias = ipv4address_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/SubnetMask"


# class HomeHubActionDeviceIPInterfacesIPv4AddressesIPv4AddressIPGatewayGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address/IPGateway"


# class HomeHubActionDeviceIPInterfacesIPv4AddressesDnsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         interface_alias: HomeHubActionXPathParamInterfaceAlias,
#         ipv4address_alias: HomeHubActionXPathParamIPv4AddressAlias,
#     ):
#         self.interface_alias = interface_alias
#         self.ipv4address_alias = ipv4address_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv4Addresses/IPv4Address[Alias='{self.ipv4address_alias.name}']/Dns"


# class HomeHubActionDeviceIPInterfacesLastChangeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/LastChange"


# class HomeHubActionDeviceIPInterfacesStatsBytesReceivedGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Stats/BytesReceived"


# class HomeHubActionDeviceIPInterfacesStatsBytesSentGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Stats/BytesSent"


# class HomeHubActionDeviceIPInterfacesStatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


# class HomeHubActionDeviceIPInterfacesStatusSubscribeForNotification(
#     HomeHubAction, MethodSubscribeForNotificationMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias, id: int):
#         self.interface_alias = interface_alias
#         self.id = id

#     @property
#     def xpath(self):
#         return f"Device/IP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

#     @property
#     def parameters(self):
#         return {"id": self.id, "type": "value-change", "current-value": False}


# class HomeHubActionDeviceManagementServerTR69InternalDataSettingsPortGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/ManagementServer/TR69InternalData/Settings/Port"


# class HomeHubActionDeviceManagersHubLightControlBrightnessGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/HubLightControl/Brightness"


# class HomeHubActionDeviceManagersHubLightControlBrightnessSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, value: any):
#         self.value = value

#     xpath = "Device/Managers/HubLightControl/Brightness"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceManagersHubLightControlFrontLEDColorGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/HubLightControl/FrontLEDColor"


# class HomeHubActionDeviceManagersHubLightControlLedEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/HubLightControl/LedEnable"


# class HomeHubActionDeviceManagersHubLightControlLedEnableSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, value: any):
#         self.value = value

#     xpath = "Device/Managers/HubLightControl/LedEnable"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceManagersHubLightControlScheduleEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/HubLightControl/Schedule/Enable"


# class HomeHubActionDeviceManagersHubLightControlScheduleEnableSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, value: any):
#         self.value = value

#     xpath = "Device/Managers/HubLightControl/Schedule/Enable"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceManagersHubLightControlScheduleTurnLightOffGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOff"


# class HomeHubActionDeviceManagersHubLightControlScheduleTurnLightOffSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, value: any):
#         self.value = value

#     xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOff"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceManagersHubLightControlScheduleTurnLightOnGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOn"


# class HomeHubActionDeviceManagersHubLightControlScheduleTurnLightOnSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, value: any):
#         self.value = value

#     xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOn"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceManagersNetworkDataDhcpLanMaxAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/NetworkData/DhcpLanMaxAddress"


# class HomeHubActionDeviceManagersNetworkDataDhcpLanMinAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/NetworkData/DhcpLanMinAddress"


# class HomeHubActionDeviceManagersNetworkDataIPv6ModeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/NetworkData/IPv6Mode"


# class HomeHubActionDeviceManagersNetworkDataIpLanGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/NetworkData/IpLan"


# class HomeHubActionDeviceManagersNetworkDataNetmaskLanGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/NetworkData/NetmaskLan"


# class HomeHubActionDeviceManagersNetworkDataObfuscatedPPPPasswordGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Managers/NetworkData/ObfuscatedPPPPassword"


# class HomeHubActionDeviceManagersNetworkDataObfuscatedPPPPasswordSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, value: any):
#         self.value = value

#     xpath = "Device/Managers/NetworkData/ObfuscatedPPPPassword"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceNATPortMappingsInternalClientGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, portmapping_alias: HomeHubActionXPathParamPortMappingAlias):
#         self.portmapping_alias = portmapping_alias

#     @property
#     def xpath(self):
#         return f"Device/NAT/PortMappings/PortMapping[Alias='{self.portmapping_alias.name}']/InternalClient"


# class HomeHubActionDeviceNATPortMappingsInternalMACAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, portmapping_alias: HomeHubActionXPathParamPortMappingAlias):
#         self.portmapping_alias = portmapping_alias

#     @property
#     def xpath(self):
#         return f"Device/NAT/PortMappings/PortMapping[Alias='{self.portmapping_alias.name}']/InternalMACAddress"


# class HomeHubActionDeviceNATPortMappingsEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, portmapping_service: HomeHubActionXPathParamPortMappingService):
#         self.portmapping_service = portmapping_service

#     @property
#     def xpath(self):
#         return f"Device/NAT/PortMappings/PortMapping[Service='{self.portmapping_service.name}']/Enable"


# class HomeHubActionDeviceNATPortMappingsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/NAT/PortMappings"


# class HomeHubActionDeviceNATSIPALGEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/NAT/SIPALGEnable"


# class HomeHubActionDevicePPPInterfacesConnectionStatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/ConnectionStatus"


# class HomeHubActionDevicePPPInterfacesIPCPLocalIPAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPCP/LocalIPAddress"


# class HomeHubActionDevicePPPInterfacesIPCPRemoteIPAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPCP/RemoteIPAddress"


# class HomeHubActionDevicePPPInterfacesIPv6CPRemoteInterfaceIdentifierGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/IPv6CP/RemoteInterfaceIdentifier"


# class HomeHubActionDevicePPPInterfacesStatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"


# class HomeHubActionDevicePPPInterfacesEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Enable"


# class HomeHubActionDevicePPPInterfacesEnableSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(
#         self, interface_alias: HomeHubActionXPathParamInterfaceAlias, value: any
#     ):
#         self.interface_alias = interface_alias
#         self.value = value

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Enable"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDevicePPPInterfacesStatusSubscribeForNotification(
#     HomeHubAction, MethodSubscribeForNotificationMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias, id: int):
#         self.interface_alias = interface_alias
#         self.id = id

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Status"

#     @property
#     def parameters(self):
#         return {"id": self.id, "type": "value-change", "current-value": False}


# class HomeHubActionDevicePPPInterfacesUsernameGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, interface_alias: HomeHubActionXPathParamInterfaceAlias):
#         self.interface_alias = interface_alias

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Username"


# class HomeHubActionDevicePPPInterfacesUsernameSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(
#         self, interface_alias: HomeHubActionXPathParamInterfaceAlias, value: any
#     ):
#         self.interface_alias = interface_alias
#         self.value = value

#     @property
#     def xpath(self):
#         return f"Device/PPP/Interfaces/Interface[Alias='{self.interface_alias.name}']/Username"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceRouterAdvertisementInterfaceSettingsAdvManagedFlagGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self, interfacesetting_alias: HomeHubActionXPathParamInterfaceSettingAlias
#     ):
#         self.interfacesetting_alias = interfacesetting_alias

#     @property
#     def xpath(self):
#         return f"Device/RouterAdvertisement/InterfaceSettings/InterfaceSetting[Alias='{self.interfacesetting_alias.name}']/AdvManagedFlag"


# class HomeHubActionDeviceRouterAdvertisementInterfaceSettingsAdvOtherConfigFlagGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self, interfacesetting_alias: HomeHubActionXPathParamInterfaceSettingAlias
#     ):
#         self.interfacesetting_alias = interfacesetting_alias

#     @property
#     def xpath(self):
#         return f"Device/RouterAdvertisement/InterfaceSettings/InterfaceSetting[Alias='{self.interfacesetting_alias.name}']/AdvOtherConfigFlag"


# class HomeHubActionDeviceServicesBandwidthMonitoringUploadBMStatisticsFile(
#     HomeHubAction, MethodUploadBMStatisticsFileMixin
# ):
#     xpath = "Device/Services/BandwidthMonitoring"

#     parameters = {"startDate": "20000101", "endDate": "20250122"}


# class HomeHubActionDeviceServicesBusinessDNSOverrideServersGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/Business/DNSOverrideServers"


# class HomeHubActionDeviceServicesBusinessDNSOverrideGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/Business/DNSOverride"


# class HomeHubActionDeviceServicesBusinessStaticIPAddressAssignationsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/Business/staticIP/AddressAssignations"


# class HomeHubActionDeviceServicesBusinessStaticIPRoutedLANEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/Business/staticIP/RoutedLANEnable"


# class HomeHubActionDeviceServicesDeviceConfigConnectionHURLPageEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/ConnectionHURLPageEnable"


# class HomeHubActionDeviceServicesDeviceConfigDomainLockListGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/DomainLockList"


# class HomeHubActionDeviceServicesDeviceConfigDomainLockingEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/DomainLockingEnable"


# class HomeHubActionDeviceServicesDeviceConfigEnableBridgedModeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/EnableBridgedMode"


# class HomeHubActionDeviceServicesDeviceConfigLastFirmwareUpgradeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/LastFirmwareUpgrade"


# class HomeHubActionDeviceServicesDeviceConfigLastSuccesfulWanTypeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/LastSuccesfulWanType"


# class HomeHubActionDeviceServicesDeviceConfigPortClampingEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/PortClampingEnable"


# class HomeHubActionDeviceServicesDeviceConfigPortClampingEnableSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, value: any):
#         self.value = value

#     xpath = "Device/Services/DeviceConfig/PortClampingEnable"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceServicesDeviceConfigWiFiModeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/WiFiMode"


# class HomeHubActionDeviceServicesDeviceConfigWifiPasswordForbiddenWordsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DeviceConfig/WifiPasswordForbiddenWords"


# class HomeHubActionDeviceServicesDynamicDNSClientsEnableSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, client_uid: int, value: any):
#         self.client_uid = client_uid
#         self.value = value

#     @property
#     def xpath(self):
#         return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Enable"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceServicesDynamicDNSClientsHostnamesNameSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, client_uid: int, hostname_uid: int, value: any):
#         self.client_uid = client_uid
#         self.hostname_uid = hostname_uid
#         self.value = value

#     @property
#     def xpath(self):
#         return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Hostnames/Hostname[@uid='{self.hostname_uid}']/Name"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceServicesDynamicDNSClientsPasswordSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, client_uid: int, value: any):
#         self.client_uid = client_uid
#         self.value = value

#     @property
#     def xpath(self):
#         return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Password"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceServicesDynamicDNSClientsServiceReferenceSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, client_uid: int, value: any):
#         self.client_uid = client_uid
#         self.value = value

#     @property
#     def xpath(self):
#         return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/ServiceReference"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceServicesDynamicDNSClientsUsernameSetValue(
#     HomeHubAction, MethodSetValueMixin
# ):
#     def __init__(self, client_uid: int, value: any):
#         self.client_uid = client_uid
#         self.value = value

#     @property
#     def xpath(self):
#         return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']/Username"

#     @property
#     def parameters(self):
#         return {
#             "value": self.value,
#         }


# class HomeHubActionDeviceServicesDynamicDNSClientsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, client_uid: int):
#         self.client_uid = client_uid

#     @property
#     def xpath(self):
#         return f"Device/Services/DynamicDNS/Clients/Client[@uid='{self.client_uid}']"


# class HomeHubActionDeviceServicesDynamicDNSServicesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/DynamicDNS/Services"


# class HomeHubActionDeviceServicesOnlineInstallDHCPFingerprintDatabaseEntriesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/OnlineInstall/DHCPFingerprintDatabase/Entries"


# class HomeHubActionDeviceServicesOnlineInstallEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/OnlineInstall/Enable"


# class HomeHubActionDeviceServicesOpenWiFiOpenWifiOptedInGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/OpenWiFi/OpenWifiOptedIn"


# class HomeHubActionDeviceServicesOpenWiFiUIEnabledGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/OpenWiFi/UIEnabled"


# class HomeHubActionDeviceServicesParentalControlGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/Services/ParentalControl"


# class HomeHubActionDeviceServicesStorageServicesLogicalVolumesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, storageservice_uid: int):
#         self.storageservice_uid = storageservice_uid

#     @property
#     def xpath(self):
#         return f"Device/Services/StorageServices/StorageService[@uid='{self.storageservice_uid}']/LogicalVolumes"


# class HomeHubActionDeviceServicesVoiceServicesCallControlLinesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         voiceservice_alias: HomeHubActionXPathParamVoiceServiceAlias,
#         line_alias: HomeHubActionXPathParamLineAlias,
#     ):
#         self.voiceservice_alias = voiceservice_alias
#         self.line_alias = line_alias

#     @property
#     def xpath(self):
#         return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/CallControl/Lines/Line[Alias='{self.line_alias.name}']"


# class HomeHubActionDeviceServicesVoiceServicesCallLogsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, voiceservice_alias: HomeHubActionXPathParamVoiceServiceAlias):
#         self.voiceservice_alias = voiceservice_alias

#     @property
#     def xpath(self):
#         return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/CallLogs"


# class HomeHubActionDeviceServicesVoiceServicesSIPClientsLastRegistrationTimeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         voiceservice_alias: HomeHubActionXPathParamVoiceServiceAlias,
#         client_alias: HomeHubActionXPathParamClientAlias,
#     ):
#         self.voiceservice_alias = voiceservice_alias
#         self.client_alias = client_alias

#     @property
#     def xpath(self):
#         return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/SIP/Clients/Client[Alias='{self.client_alias.name}']/LastRegistrationTime"


# class HomeHubActionDeviceServicesVoiceServicesSIPClientsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(
#         self,
#         voiceservice_alias: HomeHubActionXPathParamVoiceServiceAlias,
#         client_alias: HomeHubActionXPathParamClientAlias,
#     ):
#         self.voiceservice_alias = voiceservice_alias
#         self.client_alias = client_alias

#     @property
#     def xpath(self):
#         return f"Device/Services/VoiceServices/VoiceService[Alias='{self.voiceservice_alias.name}']/SIP/Clients/Client[Alias='{self.client_alias.name}']"


# class HomeHubActionDeviceUPnPDeviceUPnPIGDGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/UPnP/Device/UPnPIGD"


# class HomeHubActionDeviceUPnPSettingsExtendedUPnPSecurityGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/UPnP/Settings/ExtendedUPnPSecurity"


# class HomeHubActionDeviceUserAccountsUsersSecretQueryGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, user_login: HomeHubActionXPathParamUserLogin):
#         self.user_login = user_login

#     @property
#     def xpath(self):
#         return f"Device/UserAccounts/Users/User[Login='{self.user_login.name}']/SecretQuery"


# class HomeHubActionDeviceWiFiAccessPointsAssociatedDevicesGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
#         self.accesspoint_alias = accesspoint_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/AssociatedDevices"


# class HomeHubActionDeviceWiFiAccessPointsEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
#         self.accesspoint_alias = accesspoint_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Enable"


# class HomeHubActionDeviceWiFiAccessPointsSSIDAdvertisementEnabledGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
#         self.accesspoint_alias = accesspoint_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/SSIDAdvertisementEnabled"


# class HomeHubActionDeviceWiFiAccessPointsSecurityKeyPassphraseGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
#         self.accesspoint_alias = accesspoint_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/KeyPassphrase"


# class HomeHubActionDeviceWiFiAccessPointsSecurityModeEnabledGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
#         self.accesspoint_alias = accesspoint_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/ModeEnabled"


# class HomeHubActionDeviceWiFiAccessPointsSecurityModesSupportedGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
#         self.accesspoint_alias = accesspoint_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/ModesSupported"


# class HomeHubActionDeviceWiFiAccessPointsSecurityWEPKeyGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
#         self.accesspoint_alias = accesspoint_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/Security/WEPKey"


# class HomeHubActionDeviceWiFiAccessPointsWPSEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, accesspoint_alias: HomeHubActionXPathParamAccessPointAlias):
#         self.accesspoint_alias = accesspoint_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/AccessPoints/AccessPoint[Alias='{self.accesspoint_alias.name}']/WPS/Enable"


# class HomeHubActionDeviceWiFiQuantennaBootIPLocalGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/WiFi/Quantenna/BootIPLocal"


# class HomeHubActionDeviceWiFiQuantennaBootIPRemoteGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/WiFi/Quantenna/BootIPRemote"


# class HomeHubActionDeviceWiFiQuantennaMngtIPLocalGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/WiFi/Quantenna/MngtIPLocal"


# class HomeHubActionDeviceWiFiQuantennaMngtIPRemoteGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/WiFi/Quantenna/MngtIPRemote"


# class HomeHubActionDeviceWiFiRadiosRadioAutoChannelTriggerGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/WiFi/Radios/Radio/AutoChannelTrigger"


# class HomeHubActionDeviceWiFiRadiosRadioChannelSubscribeForNotification(
#     HomeHubAction, MethodSubscribeForNotificationMixin
# ):
#     def __init__(self, id: int):
#         self.id = id

#     xpath = "Device/WiFi/Radios/Radio/Channel"

#     @property
#     def parameters(self):
#         return {"id": self.id, "type": "value-change", "current-value": False}


# class HomeHubActionDeviceWiFiRadiosAutoChannelEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/AutoChannelEnable"


# class HomeHubActionDeviceWiFiRadiosAutoChannelTriggerGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/AutoChannelTrigger"


# class HomeHubActionDeviceWiFiRadiosChannelGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/Channel"


# class HomeHubActionDeviceWiFiRadiosChannelsInUseGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return (
#             f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/ChannelsInUse"
#         )


# class HomeHubActionDeviceWiFiRadiosEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/Enable"


# class HomeHubActionDeviceWiFiRadiosExtensionChannelGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/ExtensionChannel"


# class HomeHubActionDeviceWiFiRadiosMaxBitRateGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/MaxBitRate"


# class HomeHubActionDeviceWiFiRadiosOperatingChannelBandwidthGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/OperatingChannelBandwidth"


# class HomeHubActionDeviceWiFiRadiosOperatingStandardsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/OperatingStandards"


# class HomeHubActionDeviceWiFiRadiosPossibleChannelsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/PossibleChannels"


# class HomeHubActionDeviceWiFiRadiosTransmitPowerGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, radio_alias: HomeHubActionXPathParamRadioAlias):
#         self.radio_alias = radio_alias

#     @property
#     def xpath(self):
#         return (
#             f"Device/WiFi/Radios/Radio[Alias='{self.radio_alias.name}']/TransmitPower"
#         )


# class HomeHubActionDeviceWiFiSSIDsSSIDAliasGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     xpath = "Device/WiFi/SSIDs/SSID/Alias"


# class HomeHubActionDeviceWiFiSSIDsConnectionTimeGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
#         self.ssid_alias = ssid_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/ConnectionTime"


# class HomeHubActionDeviceWiFiSSIDsEnableGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
#         self.ssid_alias = ssid_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/Enable"


# class HomeHubActionDeviceWiFiSSIDsMACAddressGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
#         self.ssid_alias = ssid_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/MACAddress"


# class HomeHubActionDeviceWiFiSSIDsSSIDGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
#         self.ssid_alias = ssid_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/SSID"


# class HomeHubActionDeviceWiFiSSIDsStatusGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
#         self.ssid_alias = ssid_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']/Status"


# class HomeHubActionDeviceWiFiSSIDsGetValue(
#     HomeHubAction, MethodGetValueMixin, OptionsInterfaceCapabilityMixin
# ):
#     def __init__(self, ssid_alias: HomeHubActionXPathParamSSIDAlias):
#         self.ssid_alias = ssid_alias

#     @property
#     def xpath(self):
#         return f"Device/WiFi/SSIDs/SSID[Alias='{self.ssid_alias.name}']"


# class HomeHubActionDeviceArping(HomeHubAction, MethodArpingMixin):
#     xpath = "Device"


# class HomeHubActionGetEvents(HomeHubAction, MethodGetEventsMixin):
#     pass


# class HomeHubActionLogIn(HomeHubAction, MethodLogInMixin):
#     def __init__(self, user: str):
#         self.user = user

#     @property
#     def parameters(self):
#         return {
#             "user": self.user,
#             "persistent": True,
#             "session-options": {
#                 "nss": [{"name": "gtw", "uri": "http://sagemcom.com/gateway-data"}],
#                 "language": "ident",
#                 "context-flags": {"get-content-name": True, "local-time": True},
#                 "capability-depth": 2,
#                 "capability-flags": {
#                     "name": True,
#                     "default-value": False,
#                     "restriction": True,
#                     "description": False,
#                 },
#                 "time-format": "ISO_8601",
#             },
#         }


# class HomeHubActionLogOut(HomeHubAction, MethodLogOutMixin):
#     pass


# class HomeHubActionResetEvents(HomeHubAction, MethodResetEventsMixin):
#     pass


# class HomeHubActionUnsubscribeForNotification(
#     HomeHubAction, MethodUnsubscribeForNotificationMixin
# ):
#     def __init__(self, id: int):
#         self.id = id

#     @property
#     def parameters(self):
#         return {
#             "id": self.id,
#         }
