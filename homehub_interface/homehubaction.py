from abc import ABC


class HomeHubActionBase(ABC):
    def as_dict(self):
        ret = {}
        for k, v in self.__dict__.items():
            if v is None:
                continue
            elif isinstance(v, HomeHubActionBase):
                ret[k] = v.as_dict()
            else:
                ret[k] = v
        return ret


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


class HomeHubActionResetEvents(HomeHubAction):
    def __init__(self):
        self.method = "resetEvents"


class HomeHubActionHubLightControlLedEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/LedEnable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHubLightControlBrightnessGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/Brightness"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHubLightControlScheduleEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/Schedule/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHubLightControlScheduleTurnLightOnGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOn"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHubLightControlScheduleTurnLightOffGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Managers/HubLightControl/Schedule/TurnLightOff"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionHostsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Hosts/Hosts"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionGetVendorLogDownloadURI(HomeHubAction):
    def __init__(self):
        self.method = "getVendorLogDownloadURI"
        self.xpath = "Device/DeviceInfo/VendorLogFiles/VendorLogFile[@uid='1']"
        self.parameters = {"FileName": "eventLog"}
        self.admin_required = True


class HomeHubActionLogIn(HomeHubAction):
    def __init__(self, user: str):
        self.method = "logIn"
        self.parameters = {
            "user": user,
            "persistent": True,
            "session-options": {
                "nss": [
                    {
                        "name": "gtw",
                        "uri": "http://sagemcom.com/gateway-data",
                    }
                ],
                "language": "ident",
                "context-flags": {
                    "get-content-name": True,
                    "local-time": True,
                },
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


class HomeHubActionVoiceServiceLineGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/VoiceServices/VoiceService[Alias='VOICESERVICE1']/CallControl/Lines/Line[Alias='LINE1']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionVoiceServiceClientGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/VoiceServices/VoiceService[Alias='VOICESERVICE1']/SIP/Clients/Client[Alias='CLIENT1']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionVoiceServiceCallLogsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/Services/VoiceServices/VoiceService[Alias='VOICESERVICE1']/CallLogs"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionVoiceServiceClientLastRegistrationTimeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/VoiceServices/VoiceService[Alias='VOICESERVICE1']/SIP/Clients/Client[Alias='CLIENT1']/LastRegistrationTime"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionOnlineInstallEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/OnlineInstall/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfaceStatusSubscribeForNotification(HomeHubAction):
    def __init__(self):
        self.method = "subscribeForNotification"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/Status"
        self.parameters = {"id": "2", "type": "value-change", "current-value": False}


class HomeHubActionGetEvents(HomeHubAction):
    def __init__(self):
        self.method = "getEvents"


class HomeHubActionPPPInterfaceStatusSubscribeForNotification(HomeHubAction):
    def __init__(self):
        self.method = "subscribeForNotification"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/Status"
        self.parameters = {"id": "1", "type": "value-change", "current-value": False}


class HomeHubActionDeviceConfigLastSuccesfulWanTypeGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/DeviceConfig/LastSuccesfulWanType"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfaceFTTHEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfaceDSLEnableGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_DSL_DATA']/Enable"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPPPInterfaceFTTHStatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/PPP/Interfaces/Interface[Alias='PPP_FTTH_DATA']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionIPInterfaceStatusGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/Status"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionParentalControlGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/ParentalControl"
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


class HomeHubActionIPInterfaceIPv4AddressesGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/IP/Interfaces/Interface[Alias='IP_DATA']/IPv4Addresses/IPv4Address[Alias='IP_DATA_ADDRESS']/IPAddress"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionStorageServiceLogicalVolumesGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/Services/StorageServices/StorageService[@uid='1']/LogicalVolumes"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


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


class HomeHubActionHostsHistoryMaxAgeInDaysGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Hosts/HistoryMaxAgeInDays"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubAction2GSSIDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV2G']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionSecurityModePRIV0GetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/Security/ModeEnabled"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubAction2GMaxBitRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/MaxBitRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubAction2GOperatingStandardsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/OperatingStandards"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubAction2GOperatingChannelBandwidthGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/Radios/Radio[Alias='RADIO2G4']/OperatingChannelBandwidth"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionAssociatedDevicesPRIV0GetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV0']/AssociatedDevices"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubAction5GSSIDGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/SSIDs/SSID[Alias='WL_PRIV5G']"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubAction5GMaxBitRateGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/MaxBitRate"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubAction5GOperatingStandardsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/WiFi/Radios/Radio[Alias='RADIO5G']/OperatingStandards"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubAction5GOperatingChannelBandwidthGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/Radios/Radio[Alias='RADIO5G']/OperatingChannelBandwidth"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionAssociatedDevicesPRIV1GetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = (
            "Device/WiFi/AccessPoints/AccessPoint[Alias='PRIV1']/AssociatedDevices"
        )
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionPortMappingsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/NAT/PortMappings"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


class HomeHubActionStaticIPAddressAssignationsGetValue(HomeHubAction):
    def __init__(self):
        self.method = "getValue"
        self.xpath = "Device/Services/Business/staticIP/AddressAssignations"
        self.options = HomeHubActionOptions(
            capability_flags=HomeHubActionOptionsCapabilityFlags(interface=True)
        )


