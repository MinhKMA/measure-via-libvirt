import libvirt
from info_vm import utils
from info_vm import setting
from prettytable import PrettyTable


def state_vm(domain):
        dom_info = domain.info()
        state = setting.STATE_MAPPER[dom_info[0]]
        return state


def main():
    x = PrettyTable()
    x.field_names = ["Name VM", "status", "RAM total", "vCPU"]
    data = utils.ini_file_loader()
    IP_KVM = data["kvm-ip"]
    auth = [[libvirt.VIR_CRED_AUTHNAME, libvirt.VIR_CRED_PASSPHRASE], 0, None]
    conn = libvirt.openAuth('qemu+tcp://{}/system'.format(IP_KVM), auth, 0)
    for dom in conn.listAllDomains():
        state = state_vm(dom)
        x.add_row([str(dom.name()),
                   str(state),
                   str(dom.info()[2]/setting.UNITS["Ki"]),
                   str(dom.info()[3])])
    print(x)
    conn.close()


if __name__ == '__main__':
    main()