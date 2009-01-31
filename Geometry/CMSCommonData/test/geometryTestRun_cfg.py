import FWCore.ParameterSet.Config as cms

process = cms.Process("GeometryTest")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cff")

process.load("Geometry.RPCGeometry.rpcGeometry_cfi")

process.load("Geometry.DTGeometry.dtGeometry_cfi")

#startCSC
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
#process.load("Geometry.MuonCommonData.muonEndcapIdealGeometryXML_cfi")
# flags for modelling of CSC layer & strip geometry
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
#process.load("Geometry.CSCGeometryBuilder.idealForDigiCscGeometry_cff")
process.load("Alignment.CommonAlignmentProducer.FakeAlignmentSource_cfi")
#process.preferFakeAlign = cms.ESPrefer("FakeAlignmentSource", "FakeAlignmentSource")
process.fake2 = process.FakeAlignmentSource
del process.FakeAlignmentSource
process.preferFakeAlign = cms.ESPrefer("FakeAlignmentSource", "fake2")
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
#end CSC

process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")

process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")

#process.load("MagneticField.Engine.volumeBasedMagneticField_cfi")

process.load("Geometry.CaloEventSetup.CaloGeometry_cff")

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(2)
        )
process.source = cms.Source("EmptySource")

process.prpc = cms.EDAnalyzer("RPCGeometryAnalyzer")

process.pdt = cms.EDAnalyzer("DTGeometryAnalyzer")

process.pcsc = cms.EDAnalyzer("CSCGeometryAnalyzer")

process.ptrak = cms.EDAnalyzer("TrackerDigiGeometryAnalyzer")

process.pcalo = cms.EDAnalyzer("CaloGeometryAnalyzer")

process.myprint = cms.OutputModule("AsciiOutputModule")

process.MessageLogger = cms.Service("MessageLogger",
                                        detailedInfo = cms.untracked.PSet(
            threshold = cms.untracked.string('DEBUG')
                ),
                                        warning = cms.untracked.PSet(
            threshold = cms.untracked.string('WARNING')
                ),
                                        debugModules = cms.untracked.vstring('DDLParser'),
                                        critical = cms.untracked.PSet(
            threshold = cms.untracked.string('ERROR')
                ),
                                        destinations = cms.untracked.vstring('detailedInfo',
                                                                                     'critical',
                                                                                     'info',
                                                                                     'warning')
                                    )

process.p1 = cms.Path(process.pcsc*process.prpc*process.pdt*process.ptrak*process.pcalo)
process.ep = cms.EndPath(process.myprint)
