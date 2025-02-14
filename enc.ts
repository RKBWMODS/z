export function encodeToBase64(input: string): string {
    let chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    let output = "";
    let i = 0;
    let buffer: u32;

    while (i < input.length) {
        let char1 = input.charCodeAt(i++) & 0xff;
        let char2 = i < input.length ? input.charCodeAt(i++) & 0xff : 0;
        let char3 = i < input.length ? input.charCodeAt(i++) & 0xff : 0;

        buffer = (char1 << 16) | (char2 << 8) | char3;

        output += chars[(buffer >> 18) & 0x3f] +
                  chars[(buffer >> 12) & 0x3f] +
                  (i - 1 < input.length ? chars[(buffer >> 6) & 0x3f] : "=") +
                  (i < input.length ? chars[buffer & 0x3f] : "=");
    }

    return output;
}
